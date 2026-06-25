package com.example.kafka.order.entity;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "failed_order_commands")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class FailedOrderCommand {

    @Id
    @GeneratedValue
    private Long id;

    private String originalTopic;

    private Integer originalPartition;

    private Long originalOffset;

    private String messageKey;

    @Column(columnDefinition = "TEXT")
    private String payloadJson;

    @Column(columnDefinition = "TEXT")
    private String reason;

    private LocalDateTime failedAt;

    @Enumerated(EnumType.STRING)
    private FailedOrderCommandStatus status;

    private LocalDateTime replayedAt;

    @Column(columnDefinition = "TEXT")
    private String replayError;
}
