package com.example.kafka.order.deadletter;

public enum DeadLetterStatus {
    PENDING,
    REPLAYED,
    REPLAY_FAILED
}
