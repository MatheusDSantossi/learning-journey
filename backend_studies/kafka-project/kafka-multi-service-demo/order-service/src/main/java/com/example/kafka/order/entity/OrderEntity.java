package com.example.kafka.order.entity;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "orders",
    uniqueConstraints = @UniqueConstraint(name = "uk_orders_order_id", columnNames = "orderId")
)
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class OrderEntity {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Long id;
    
    private String orderId;

    private String customerId;

    private Double amount;

    private LocalDateTime createdAt;
}
