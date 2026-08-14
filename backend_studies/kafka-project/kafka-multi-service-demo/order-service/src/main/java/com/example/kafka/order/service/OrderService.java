package com.example.kafka.order.service;

import java.time.LocalDateTime;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.dto.OrderCreatedEvent;
import com.example.kafka.order.entity.OrderEntity;
import com.example.kafka.order.outbox.OutboxEvent;
import com.example.kafka.order.outbox.OutboxEventRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;
// import com.example.kafka.order.producer.OrderCreatedProducer;
import com.example.kafka.order.repository.OrderRepository;

@Service
public class OrderService {
    private final OrderRepository orderRepository;
    // private final OrderCreatedProducer producer;
    private final OutboxEventRepository outboxEventRepository;
    private final ObjectMapper objectMapper;

    public OrderService(OrderRepository orderRepository, OutboxEventRepository outboxEventRepository, ObjectMapper objectMapper) {
        this.orderRepository = orderRepository;
        // this.producer = producer;
        this.outboxEventRepository = outboxEventRepository;
        this.objectMapper = objectMapper;
    }

    @Transactional
    public void handle(CreateOrderCommand command, String correlationId) {

        if (command == null) {
            throw new IllegalArgumentException("Order command cannot be null");
        }

        if (command.getOrderId() == null || command.getOrderId().isBlank()) {
            throw new IllegalArgumentException("orderId cannot be null or blank");
        }

        if (orderRepository.existsByOrderId(command.getOrderId())) {
            System.out.println("Duplicate order ignored: " + command.getOrderId());
            return;
        }

        if ("ORD-FAIL".equals(command.getOrderId())) {
            throw new RuntimeException("Simulated DB failure");
            
        }
        
        OrderEntity order = OrderEntity.builder().orderId(command.getOrderId())
                .customerId(command.getCustomerId())
                .amount(command.getAmount())
                .createdAt(LocalDateTime.now())
                .build();

        
        
        orderRepository.save(order);

        OrderCreatedEvent event = new OrderCreatedEvent(
                command.getOrderId(),
                command.getCustomerId(),
                command.getAmount());

        String payload;

        try {
            payload = objectMapper.writeValueAsString(event);
        } catch (JsonProcessingException e) {
            throw new IllegalStateException("Failed to serialized OrderCreatedEvent", e);
        }
        OutboxEvent outboxEvent = OutboxEvent.builder().eventType("OrderCreatedEvent").aggregateType("Order").aggregateId(command.getOrderId()).payload(payload).correlationId(correlationId).createdAt(LocalDateTime.now()).build();

        outboxEventRepository.save(outboxEvent);

        System.out.println("Order saved to PostgreSQL: " + command.getOrderId());
        System.out.println("Outbox event saved: " + outboxEvent.getId());

        // producer.send(event, correlationId);
    }
}
