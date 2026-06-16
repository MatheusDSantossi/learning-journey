package com.example.kafka.payment.producer;

import com.example.kafka.payment.dto.PaymentApprovedEvent;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class PaymentApprovedProducer {
    private final KafkaTemplate<String, PaymentApprovedEvent> kafkaTemplate;

    public PaymentApprovedProducer(KafkaTemplate<String, PaymentApprovedEvent> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void send(PaymentApprovedEvent event) {
        kafkaTemplate.send("payments.approved", event.getOrderId(), event);
        System.out.println("Sent PaymentApproved event: " + event);
    }
}