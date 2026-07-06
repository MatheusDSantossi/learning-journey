package com.example.kafka.payment.producer;

import com.example.kafka.payment.dto.PaymentApprovedEvent;

import lombok.RequiredArgsConstructor;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PaymentApprovedProducer {
    public static final String TOPIC = "payments.approved";
    public static final String CORRELATION_ID_HEADER = "X-Correlation-Id";

    private final KafkaTemplate<String, PaymentApprovedEvent> kafkaTemplate;

    public PaymentApprovedProducer(KafkaTemplate<String, PaymentApprovedEvent> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void send(PaymentApprovedEvent event) {
        Message<PaymentApprovedEvent> message = MessageBuilder.withPayload(event).setHeader(KafkaHeaders.TOPIC, TOPIC).setHeader(CORRELATION_ID_HEADER, correlationId).build();

        kafkaTemplate.send(message);
        System.out.println("Sent PaymentApproved event: " + event);
    }
}