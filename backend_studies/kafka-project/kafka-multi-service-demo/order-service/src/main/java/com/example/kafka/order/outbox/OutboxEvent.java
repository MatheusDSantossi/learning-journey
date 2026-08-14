package com.example.kafka.order.outbox;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "outbox_events")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class OutboxEvent {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String eventType;
    
    private String aggregateType;

    private String aggregateId;

    @Column(columnDefinition = "TEXT")
    private String payload;

    private String correlationId;

    private LocalDateTime createdAt;

    private LocalDateTime publishedAt;
}
