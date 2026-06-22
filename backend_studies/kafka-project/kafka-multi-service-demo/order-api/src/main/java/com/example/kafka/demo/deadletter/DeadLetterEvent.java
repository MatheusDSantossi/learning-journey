package com.example.kafka.demo.deadletter;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

import com.example.kafka.demo.deadletter.DeadLetterStatus;

@Entity
@Table(name = "dead_letter_events")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DeadLetterEvent {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String originalTopic;

    private Integer originalPartition;

    private Long originalOffset;

    private String messageKey;

    @Column(columnDefinition = "TEXT")
    private String payloadJson;

    @Column(columnDefinition = "TEXT")
    private String exceptionMessage;

    private LocalDateTime failedAt;

    @Enumerated(EnumType.STRING)
    private DeadLetterStatus status;

    private LocalDateTime replayedAt;

    @Column(columnDefinition = "TEXT")
    private String replayError;

    private Integer replayAttempts;
}
