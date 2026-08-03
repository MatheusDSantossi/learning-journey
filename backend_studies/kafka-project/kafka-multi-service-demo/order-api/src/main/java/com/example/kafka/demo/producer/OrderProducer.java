package com.example.kafka.demo.producer;

import com.example.kafka.order.dto.CreateOrderCommand;
import lombok.RequiredArgsConstructor;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class OrderProducer {
    public static final String TOPIC = "orders.commands";
    public static final String CORRELATION_ID_HEADER = "X-Correlation-Id";

    private final KafkaTemplate<String, CreateOrderCommand> kafkaTemplate;

    public void send(CreateOrderCommand command, String correlationId) {
        Message<CreateOrderCommand> message = MessageBuilder.withPayload(command).setHeader(KafkaHeaders.TOPIC, TOPIC)
                .setHeader(CORRELATION_ID_HEADER, correlationId).build();

        kafkaTemplate.send(message);

        System.out.println("Sent OrderCreated command: " + command);
    }
}
