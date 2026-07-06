package com.example.kafka.order.consumer;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.service.OrderService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class CreateOrderCommandConsumer {
    private final OrderService orderService;

    public CreateOrderCommandConsumer(OrderService orderService) {
        this.orderService = orderService;
    }

    @KafkaListener(topics = "orders.commands", groupId = "order-service-group")
    public void consume(ConsumerRecord<String, CreateOrderCommand> record, @Header(value = "X-Correlation-Id", required = false)  String correlationId, Acknowledgment acknowledgment) {

        System.out.println("Received CreateOrderCommand: " + record.value());

        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString() : correlationId;

        MDC.put("correlationId", finalCorrelationid);

        try {
            log.info("Received CreateOrderCommand");
            orderService.handle(record.value());
            acknowledgment.acknowledge();
        } finally {
            MDC.remove("correlationId");
        }

    }
}
