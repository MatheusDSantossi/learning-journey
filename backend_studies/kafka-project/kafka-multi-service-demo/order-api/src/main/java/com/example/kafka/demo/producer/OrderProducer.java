package com.example.kafka.demo.producer;

import com.example.kafka.demo.dto.CreateOrderCommand;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderProducer {
    private final KafkaTemplate<String, CreateOrderCommand> kafkaTemplate;

    public void send(CreateOrderCommand command) {
        kafkaTemplate.send(
                // "orders",
                "orders.commands",
                command.getCustomerId(), // !IMPORTANT: It's Kafka key, this means all orders from the same customer will
                                       // go to the same partition
                command);

        System.out.println("Sent OrderCreated command: " + command);
    }
}
