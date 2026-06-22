package com.example.kafka.demo.deadletter;

public enum DeadLetterStatus {
    PENDING,
    REPLAYED,
    REPLAY_FAILED
}
