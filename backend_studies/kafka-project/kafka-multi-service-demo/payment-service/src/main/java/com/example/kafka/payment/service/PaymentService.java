package com.example.kafka.payment.service;

import com.example.kafka.payment.dto.OrderCreatedEvent;
import com.example.kafka.payment.dto.PaymentApprovedEvent;
import com.example.kafka.payment.producer.PaymentApprovedProducer;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.UUID;

@Service
public class PaymentService {
    private final PaymentApprovedProducer paymentApprovedProducer;

    public PaymentService(PaymentApprovedProducer paymentApprovedProducer) {
        this.paymentApprovedProducer = paymentApprovedProducer;
    }

    public void process(OrderCreatedEvent event) {
        System.out.println("Processing payment for order: " + event.getOrderId());

        PaymentApprovedEvent approvedEvent = new PaymentApprovedEvent(
            event.getOrderId(),
            UUID.randomUUID().toString(),
            LocalDateTime.now().toString()
        );

        paymentApprovedProducer.send(approvedEvent);
 
    }
}
