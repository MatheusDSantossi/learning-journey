package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import com.example.kafka.demo.entity.OrderEntity;
import com.example.kafka.demo.repository.OrderRepository;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class OrderConsumer {
    private final OrderRepository orderRepository;

    public OrderConsumer(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    @KafkaListener(topics = "orders", groupId = "order-group")
    public void consume(ConsumerRecord<String, OrderCreatedEvent> record, Acknowledgment acknowledgment) {
        OrderCreatedEvent event = record.value();

        System.out.println("Received event: " + event);

        if (orderRepository.existsByOrderId(event.getOrderId())) {
            System.out.println("Duplicate order ignored: " + event.getOrderId());
            acknowledgment.acknowledge();
            return;
        }

        OrderEntity order = OrderEntity.builder().orderId(event.getOrderId()).customerId(event.getCustomerId()).amount(event.getAmount()).createdAt(LocalDateTime.now()).build();

        orderRepository.save(order);

        System.out.println("Order saved to PostgreSQL: " + event.getOrderId());

        acknowledgment.acknowledge();
    }
}
