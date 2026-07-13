package com.example.kafka.payment.producer;

import com.example.kafka.payment.dto.PaymentApprovedEvent;

import lombok.RequiredArgsConstructor;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Service;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Service
@RequiredArgsConstructor
public class PaymentApprovedProducer {
    public static final String TOPIC = "payments.approved";
    public static final String CORRELATION_ID_HEADER = "X-Correlation-Id";

    private final KafkaTemplate<String, PaymentApprovedEvent> kafkaTemplate;

    public void send(PaymentApprovedEvent event, String correlationId) {
        Message<PaymentApprovedEvent> message = MessageBuilder.withPayload(event).setHeader(KafkaHeaders.TOPIC, TOPIC).setHeader(CORRELATION_ID_HEADER, correlationId).build();

        log.info("payment-service publishing PaymentApprovedEvent with correlationId={}", correlationId);

        kafkaTemplate.send(message);
        System.out.println("Sent PaymentApproved event: " + event);
    }
}