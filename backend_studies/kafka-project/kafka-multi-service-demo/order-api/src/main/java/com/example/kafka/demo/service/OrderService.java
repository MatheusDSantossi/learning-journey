package com.example.kafka.demo.service;

import com.example.kafka.demo.dto.CreateOrderCommand;
import com.example.kafka.demo.entity.OrderEntity;
import com.example.kafka.demo.metrics.KafkaMetricsService;
import com.example.kafka.demo.repository.OrderRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final KafkaMetricsService kafkaMetricsService;

    public OrderService(OrderRepository orderRepository, KafkaMetricsService kafkaMetricsService) {
        this.orderRepository = orderRepository;
        this.kafkaMetricsService = kafkaMetricsService;
    }

    @Transactional
    public void handleOrderCreated(CreateOrderCommand event) {
        var sample = kafkaMetricsService.startOrderProcessingTimer();

        try {

            if (event == null) {
                throw new IllegalArgumentException("Order event cannot be null");
            }

            if (event.getOrderId() == null || event.getOrderId().isBlank()) {
                throw new IllegalArgumentException("orderId cannot be null or blank");
            }

            // if ("ORD-DLT".equals(event.getOrderId())) {
            // throw new RuntimeException("Simulated database failure");
            // }

            if (orderRepository.existsByOrderId(event.getOrderId())) {
                System.out.println("Duplicate order ignored: " + event.getOrderId());
                return;
            }

            OrderEntity order = OrderEntity.builder().orderId(event.getOrderId()).customerId(event.getCustomerId())
                    .amount(event.getAmount()).createdAt(LocalDateTime.now()).build();

            orderRepository.save(order);

            kafkaMetricsService.incrementOrderProcessed();
            System.out.println("Order saved to PostgreSQL: " + event.getOrderId());
        } catch (RuntimeException e) {
            kafkaMetricsService.incrementOrderFailed();
            throw e;
        } finally {
            sample.stop(kafkaMetricsService.orderProcessingTimer());
        }
    }
}
