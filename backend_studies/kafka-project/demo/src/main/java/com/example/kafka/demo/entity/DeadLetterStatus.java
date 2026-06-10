package com.example.kafka.demo.entity;

public enum DeadLetterStatus {
    PENDING,
    REPLAYED,
    REPLAY_FAILED
}
