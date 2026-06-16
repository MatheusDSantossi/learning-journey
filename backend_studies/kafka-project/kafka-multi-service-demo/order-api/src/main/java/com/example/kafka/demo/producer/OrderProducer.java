package com.example.kafka.demo.producer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderProducer {
    private final KafkaTemplate<String, OrderCreatedEvent> kafkaTemplate;

    public void send(OrderCreatedEvent event) {
        kafkaTemplate.send(
                // "orders",
                "orders.created",
                event.getCustomerId(), // !IMPORTANT: It's Kafka key, this means all orders from the same customer will
                                       // go to the same partition
                event);

        System.out.println("Sent OrderCreated event: " + event);
    }
}
