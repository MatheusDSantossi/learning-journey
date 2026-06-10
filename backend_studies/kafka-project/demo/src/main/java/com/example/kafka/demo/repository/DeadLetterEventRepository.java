package com.example.kafka.demo.repository;

import com.example.kafka.demo.entity.DeadLetterEvent;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface DeadLetterEventRepository extends JpaRepository<DeadLetterEvent, Long> {
    List<DeadLetterEvent> findByReplayedFalseOrderByFailedAtDesc();
}
