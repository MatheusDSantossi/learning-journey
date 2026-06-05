package com.example.kafka.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.kafka.demo.entity.OrderEntity;

public interface OrderRepository extends JpaRepository<OrderEntity, Long> {
    boolean existsByOrderId(String orderId);
}
