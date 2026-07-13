package com.example.kafka.order.consumer;

import java.util.UUID;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.service.OrderService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.slf4j.MDC;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class CreateOrderCommandConsumer {
    private final OrderService orderService;

    @KafkaListener(topics = "orders.commands", groupId = "order-service-group")
    public void consume(ConsumerRecord<String, CreateOrderCommand> record,
            @Header(value = "X-Correlation-Id", required = false) String correlationId, Acknowledgment acknowledgment) {

        System.out.println("Received CreateOrderCommand: " + record.value());

        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString()
                : correlationId;

        log.info("order-service received correlationId={}", finalCorrelationId);
        MDC.put("correlationId", finalCorrelationId);

        try {
            log.info("Received CreateOrderCommand");
            orderService.handle(record.value(), finalCorrelationId);
            acknowledgment.acknowledge();
        } finally {
            MDC.remove("correlationId");
        }

    }
}
