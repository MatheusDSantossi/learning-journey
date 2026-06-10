package com.example.kafka.demo.service;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import com.example.kafka.demo.entity.DeadLetterEvent;
import com.example.kafka.demo.repository.DeadLetterEventRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public class DeadLetterService {
    private final DeadLetterEventRepository repository;
    private final KafkaTemplate<String, OrderCreatedEvent> kafkaTemplate;
    private final ObjectMapper objectMapper;

    public DeadLetterService(
            DeadLetterEventRepository repository,
            KafkaTemplate<String, OrderCreatedEvent> kafkaTemplate,
            ObjectMapper objectMapper) {
        this.repository = repository;
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
    }

    @Transactional
    public void storeFailedEvent(
            String originalTopic,
            Integer originalPartition,
            Long originalOffset,
            String messageKey,
            OrderCreatedEvent payload,
            String exceptionMessage) {
        try {
            DeadLetterEvent dlt = DeadLetterEvent.builder()
                    .originalTopic(originalTopic)
                    .originalPartition(originalPartition)
                    .originalOffset(originalOffset)
                    .messageKey(messageKey)
                    .payloadJson(objectMapper.writeValueAsString(payload))
                    .exceptionMessage(exceptionMessage)
                    .failedAt(LocalDateTime.now())
                    .replayed(false)
                    .build();

            System.out.println("DLT payload class: " + payload.getClass());
            System.out.println("DLT payload json: " + objectMapper.writeValueAsString(payload));
            System.out.println("DLT exception message: " + exceptionMessage);

            repository.save(dlt);

            System.out.println("Saved failed event to DB: " + dlt.getId());
        } catch (Exception e) {
            throw new RuntimeException("Failed to store dead-letter event", e);
        }
    }

    @Transactional
    public void replay(Long id) {
        DeadLetterEvent dlt = repository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("DLT Event not found: " + id));

        if (dlt.isReplayed()) {
            System.out.println("Event already replayed: " + id);
            return;
        }

        try {
            OrderCreatedEvent event = objectMapper.readValue(
                    dlt.getPayloadJson(),
                    OrderCreatedEvent.class);

            kafkaTemplate.send(
                    dlt.getOriginalTopic(),
                    dlt.getMessageKey(),
                    event);

            dlt.setReplayed(true);
            dlt.setReplayedAt(LocalDateTime.now());
            repository.save(dlt);

            System.out.println("Replayed dead-letter event: " + id);
        } catch (Exception e) {
            throw new RuntimeException("Failed to replay dead-letter event " + id, e);
        }
    }
}
