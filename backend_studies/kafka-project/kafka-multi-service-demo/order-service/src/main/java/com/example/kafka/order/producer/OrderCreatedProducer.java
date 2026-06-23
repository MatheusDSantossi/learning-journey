package com.example.kafka.order.producer;

import com.example.kafka.order.dto.OrderCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderCreatedProducer {

    private final KafkaTemplate<String, OrderCreatedEvent> kafkaTemplate;

    public void send(OrderCreatedEvent event) {
        kafkaTemplate.send(
                "orders.created",
                event.getCustomerId(),
                event);

        System.out.println("Sent OrderCreatedEvent: " + event);
    }
}
