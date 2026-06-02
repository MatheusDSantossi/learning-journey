package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class OrderConsumer {
    @KafkaListener(
        topics = "orders",
        groupId = "order-group"
    )

    public void consumer(OrderCreatedEvent event) {
         System.out.println(
            "Received order: " + event
        );
    }
}
