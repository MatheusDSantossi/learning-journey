package com.example.kafka.order.outbox;

import com.example.kafka.order.dto.OrderCreatedEvent;
import com.fasterxml.jackson.databind.ObjectMapper;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsCosntructor
@Slf4j
public class OutboxPublisher {
    private final OutboxEventRepository outboxEventRepository;
    private final KafkaTempalte<String, Object> kafkaTemplate;
    private final ObjectMapper objectMapper;

    @Scheduled(fixedDelay = 5000)
    public void publishPendingEvents() {
        List<OutboxEvent> events = outboxEventRepository.findByPublishedAtIsNullOrderByCreatedAtAsc();

        if (events.isEmpty()) {
            return;
        }

        log.info("Found {} pending outbox event(s)", events.size());

        for (OutboxEvent event : events) {
            try {
                publish(event);
            } catch (Exception e) {
                log.error("Failed to publish outbox event id={} aggregateId = {}",
                    event.getId(),
                    event.getAggregateId(),
                    e
                );
            }
        }
    }

    @Transactional
    public void publish(OutboxEvent outboxEvent) throws Exception {
        if (!"OrderCreatedEvent".equals(outboxEvent.getEventType())) {
            throw new IllegalArgumentException("Unsupported event type: " + outboxEvent.getEventType());
        }

        OrderCreatedEvent event = objectMapper.readValue(
            outboxEvent.getPayload(),
            OrderCreatedEvent.class
        );

        Message<OrderCreatedEvent> message = MessageBuilder.withPayload(event).setHeader(KafkaHeaders.TOPIC, "orders.created").setHeader(KafkaHeaders.KEY, outboxEvent.getAggregateId()).setHeader("X-Correlation-Id", outboxEvent.getCorrelationId()).build();

        log.info("Publishing outbox event id={} aggregateId={} correlationId={}", outboxEvent.getId(), outboxEvent.getAggregateId(), outboxEvent.getCorrelationId());

        // Wait for Kafka to confirm the send.
        kafkaTemplate.send(message).get();

        outboxEvent.setPublishedAt(LocalDateTime.now());
        outboxEventRepository.save(outboxEvent);

        log.info(
            "Outbox event published successfuly id={} aggregateId={}",
            outboxEvent.getId(),
            outboxEvent.getAggregateId()
        );
    }
}
