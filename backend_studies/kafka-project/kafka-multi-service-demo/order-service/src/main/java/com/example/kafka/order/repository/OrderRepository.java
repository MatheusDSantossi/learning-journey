package com.example.kafka.order.repository;

import com.example.kafka.order.entity.OrderEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRepository extends JpaRepository<OrderEntity, Long> {
    boolean existsByOrderId(String orderId);
}
