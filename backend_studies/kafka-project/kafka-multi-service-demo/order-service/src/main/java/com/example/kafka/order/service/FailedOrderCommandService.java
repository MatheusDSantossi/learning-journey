package com.example.kafka.order.service;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.entity.FailedOrderCommand;
import com.example.kafka.order.entity.FailedOrderCommandStatus;
import com.example.kafka.order.repository.FailedOrderCommandRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import com.example.kafka.order.dto.OrderCreatedEvent;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class FailedOrderCommandService {
    private final FailedOrderCommandRepository failedOrderCommandRepository;
    private final KafkaTemplate<String, Object> kafkaTemplate;
    private final ObjectMapper objectMapper;

    public FailedOrderCommandService(
            FailedOrderCommandRepository failedOrderCommandRepository,
            KafkaTemplate<String, Object> kafkaTemplate,
            ObjectMapper objectMapper) {
        this.failedOrderCommandRepository = failedOrderCommandRepository;
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
    }

    @Transactional
    public void storeFailedEvent(
            String originalTopic,
            Integer originalPartition,
            Long originalOffset,
            String messageKey,
            CreateOrderCommand payload,
            String exceptionMessage) {
        try {
            FailedOrderCommand failed = FailedOrderCommand.builder().originalTopic(originalTopic)
                    .originalPartition(originalPartition).originalOffset(originalOffset).messageKey(messageKey)
                    .payloadJson(objectMapper.writeValueAsString(payload)).reason(exceptionMessage)
                    .failedAt(LocalDateTime.now()).status(FailedOrderCommandStatus.PENDING).build();

            failedOrderCommandRepository.save(failed);

            System.out.println("Saved failed order command to DB: " + failed.getId());
        } catch (Exception e) {
            throw new RuntimeException("Failed to store dead-letter order command", e);
        }
    }

    @Transactional
    public void replay(Long id) {
        FailedOrderCommand failed = failedOrderCommandRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Failed order command not found"));

        if (failed.getStatus() == FailedOrderCommandStatus.REPLAYED) {
            System.out.println("Order command already replayed: " + id);
            return;
        }

        try {
            CreateOrderCommand command = objectMapper.readValue(failed.getPayloadJson(),
                    CreateOrderCommand.class);

            kafkaTemplate.send(
                    "orders.commands",
                    command).get();

            failed.setStatus(FailedOrderCommandStatus.REPLAYED);
            failed.setReplayedAt(LocalDateTime.now());
            failed.setReplayError(null);
            failedOrderCommandRepository.save(failed);

            System.out.println("Replayed failed order command: " + id);
        } catch (Exception e) {
            failed.setStatus(FailedOrderCommandStatus.REPLAY_FAILED);
            failed.setReplayError(e.getClass().getSimpleName() + ": " + e.getMessage());
            failedOrderCommandRepository.save(failed);

            throw new RuntimeException("Failed to replay failed order command " + id, e);

        }
    }

    @Transactional
    public int replayAllPending() {
        List<FailedOrderCommand> pending = failedOrderCommandRepository
                .findByStatusOrderByFailedAtDesc(FailedOrderCommandStatus.PENDING);

        int replayed = 0;

        for (FailedOrderCommand failed : pending) {
            try {
                replay(failed.getId());
                replayed++;
            } catch (Exception e) {
                System.out.println("Replay failed for id " + failed.getId() + ": " + e.getMessage());
            }
        }

        return replayed;
    }
}