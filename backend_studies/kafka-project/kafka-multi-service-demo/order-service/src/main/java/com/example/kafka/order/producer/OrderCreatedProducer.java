package com.example.kafka.order.producer;

import com.example.kafka.order.dto.OrderCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderCreatedProducer {

    public static final String TOPIC = "orders.created";
    public static final String CORRELATION_ID_HEADER = "X-Correlation-Id";

    private final KafkaTemplate<String, Object> kafkaTemplate;

    public void send(OrderCreatedEvent event, String correlationId) {
        Message<OrderCreatedEvent> message = MessageBuilder.withPayload(event).setHeader(KafkaHeaders.TOPIC, topic).setHeader(CORRELATION_ID_HEADER, correlationId).build();

        kafkaTemplate.send(message);

        System.out.println("Sent OrderCreatedEvent: " + event);
    }
}
