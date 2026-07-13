package com.example.kafka.payment.service;

import java.util.UUID;

import com.example.kafka.payment.dto.CreateOrderCommand;
import com.example.kafka.payment.dto.PaymentApprovedEvent;
import com.example.kafka.payment.producer.PaymentApprovedProducer;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Service
public class PaymentService {
    private final PaymentApprovedProducer paymentApprovedProducer;

    public PaymentService(PaymentApprovedProducer paymentApprovedProducer) {
        this.paymentApprovedProducer = paymentApprovedProducer;
    }

    public void process(CreateOrderCommand event, String correlationId) {
        System.out.println("Processing payment for order: " + event.getOrderId());

        PaymentApprovedEvent approvedEvent = new PaymentApprovedEvent(
                event.getOrderId(),
                UUID.randomUUID().toString(),
                LocalDateTime.now().toString());

        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString()
                : correlationId;

        log.info("payment-service received correlationId={}", finalCorrelationId);

        paymentApprovedProducer.send(approvedEvent, finalCorrelationId);

    }
}
