package com.example.kafka.payment.consumer;

import com.example.kafka.payment.dto.CreateOrderCommand;
import com.example.kafka.payment.service.PaymentService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class OrderCreatedConsumer {
    private final PaymentService paymentService;

    public OrderCreatedConsumer(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @KafkaListener(topics = "orders.created", groupId = "payment-group")
    public void consume(ConsumerRecord<String, CreateOrderCommand> record,  @Header(value = "X-Correlation-Id", required = false) String correlationId, Acknowledgment acknowledgment) {
        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString() : correlationId;

        MDC.put("correlationId", finalCorrelationId);

        try {
            log.info("Received OrderCreatedEvent");
            CreateOrderCommand event = record.value();
    
            System.out.println("Received OrderCreated event: " + event);
    
            paymentService.process(event, finalCorrelationId);
    
            acknowledgment.acknowledge();

        } finally {
            MDC.remove("correlationId");
        }

    }
}
