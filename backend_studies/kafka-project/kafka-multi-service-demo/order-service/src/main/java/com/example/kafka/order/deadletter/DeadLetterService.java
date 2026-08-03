package com.example.kafka.order.deadletter;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.metrics.KafkaMetricsService;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.kafka.support.KafkaHeaders;

import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;

import java.time.LocalDateTime;

@Service
public class DeadLetterService {
    private final DeadLetterEventRepository repository;
    private final KafkaTemplate<String, Object> kafkaTemplate;
    private final ObjectMapper objectMapper;
    private final KafkaMetricsService kafkaMetricsService;

    public DeadLetterService(
            DeadLetterEventRepository repository,
            KafkaTemplate<String, Object> kafkaTemplate,
            ObjectMapper objectMapper,
            KafkaMetricsService kafkaMetricsService) {
        this.repository = repository;
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
        this.kafkaMetricsService = kafkaMetricsService;
    }

    @Transactional
    public void storeFailedEvent(
            String originalTopic,
            Integer originalPartition,
            Long originalOffset,
            String messageKey,
            CreateOrderCommand payload,
            String correlationId,
            String exceptionMessage) {
        try {
            DeadLetterEvent dlt = DeadLetterEvent.builder()
                    .originalTopic(originalTopic)
                    .originalPartition(originalPartition)
                    .originalOffset(originalOffset)
                    .messageKey(messageKey)
                    .correlationId(correlationId)
                    .payloadJson(objectMapper.writeValueAsString(payload))
                    .exceptionMessage(exceptionMessage)
                    .failedAt(LocalDateTime.now()).status(DeadLetterStatus.PENDING)
                    .build();
            // .replayed(false)

            System.out.println("DLT payload class: " + payload.getClass());
            System.out.println("DLT payload json: " + objectMapper.writeValueAsString(payload));
            System.out.println("DLT exception message: " + exceptionMessage);

            repository.save(dlt);

            kafkaMetricsService.incrementDltStored();

            System.out.println("Saved failed event to DB: " + dlt.getId());
        } catch (Exception e) {
            throw new RuntimeException("Failed to store dead-letter event", e);
        }
    }

    @Transactional
    public void replay(Long id) {
        var sample = kafkaMetricsService.startDltReplayTimer();

        try {
            DeadLetterEvent dlt = repository.findById(id)
                    .orElseThrow(() -> new IllegalArgumentException("DLT Event not found: " + id));

            System.out.println(
                    "[DLT] Replay successful | " +
                            "id=" + id +
                            " topic=" + dlt.getOriginalTopic() +
                            " key=" + dlt.getMessageKey());

            if (dlt.getStatus() == DeadLetterStatus.REPLAYED) {
                System.out.println("Event already replayed: " + id);
                return;
            }

            CreateOrderCommand event = objectMapper.readValue(
                    dlt.getPayloadJson(),
                    CreateOrderCommand.class);

            Message<CreateOrderCommand> message = MessageBuilder.withPayload(event)
                    .setHeader(KafkaHeaders.TOPIC, dlt.getOriginalTopic())
                    .setHeader(KafkaHeaders.KEY, dlt.getMessageKey())
                    .setHeader("X-Correlation-Id", dlt.getCorrelationId()).build();

            kafkaTemplate.send(message);
            // kafkaTemplate.send(
            // dlt.getOriginalTopic(),
            // dlt.getMessageKey(),
            // event);

            dlt.setStatus(DeadLetterStatus.REPLAYED);
            dlt.setReplayedAt(LocalDateTime.now());
            dlt.setReplayError(null);
            // dlt.setReplayAttempts(dlt.getReplayAttempts() + 1);
            Integer attempts = dlt.getReplayAttempts();

            dlt.setReplayAttempts(attempts == null ? 1 : attempts + 1);

            repository.save(dlt);

            kafkaMetricsService.incrementDltReplayed();

            System.out.println("[DLT] Replay successful | id=" + id +
                    " topic=" + dlt.getOriginalTopic() +
                    " key=" + dlt.getMessageKey());
        } catch (Exception e) {
            kafkaMetricsService.incrementDltReplayFailed();

            System.err.println("[DLT] Replay failed | id=" + id +
                    " reason=" + e.getMessage());

            DeadLetterEvent dlt = repository.findById(id)
                    .orElseThrow(() -> new IllegalArgumentException("DLT event not found: " + id));

            dlt.setStatus(DeadLetterStatus.REPLAY_FAILED);
            dlt.setReplayError(e.getClass().getSimpleName() + ": " + e.getMessage());
            repository.save(dlt);

            System.err.println(
                    "[DLT] Replay failed | " +
                            "id=" + id +
                            " reason=" + e.getMessage());

            throw new RuntimeException("Failed to replay dead-letter event " + id, e);
        } finally {
            sample.stop(kafkaMetricsService.dltReplayTimer());
        }
    }

    @Transactional
    public int replayAllPending() {
        var pending = repository.findByStatusOrderByFailedAtDesc(DeadLetterStatus.PENDING);

        int replayedCount = 0;
        for (DeadLetterEvent dlt : pending) {
            try {
                replay(dlt.getId());
                replayedCount++;
            } catch (Exception e) {
                System.out.println("Failed to replay DLT event " + dlt.getId() + ": " + e.getMessage());
            }
        }

        return replayedCount;

    }
}
