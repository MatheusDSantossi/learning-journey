package com.example.kafka.demo.deadletter;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface DeadLetterEventRepository extends JpaRepository<DeadLetterEvent, Long> {
    List<DeadLetterEvent> findByStatusOrderByFailedAtDesc(DeadLetterStatus status);
}
