package com.example.kafka.order.service;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.dto.OrderCreatedEvent;
import com.example.kafka.order.entity.OrderEntity;
import com.example.kafka.order.producer.OrderCreatedProducer;
import com.example.kafka.order.repository.OrderRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final OrderCreatedProducer producer;

    public OrderService(OrderRepository orderRepository, OrderCreatedProducer producer) {
        this.orderRepository = orderRepository;
        this.producer = producer;
    }

    @Transactional
    public void handle(CreateOrderCommand command) {
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

        OrderEntity order = OrderEntity.builder().orderId(command.getOrderId())
                .customerId(command.getCustomerId())
                .amount(command.getAmount())
                .createdAt(LocalDateTime.now())
                .build();

        orderRepository.save(order);

        System.out.prinln("Order saved to PostgreSQL: " + command.getOrderId());

        OrderCreatedEvent event = new OrderCreatedEvent(
            command.getOrderId(),
            command.getCustomerId(),
            command.getAmount()
        );
    }
}
