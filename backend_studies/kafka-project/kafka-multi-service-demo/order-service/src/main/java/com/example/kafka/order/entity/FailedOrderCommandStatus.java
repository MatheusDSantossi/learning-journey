package com.example.kafka.order.entity;

public enum FailedOrderCommandStatus {
    PENDING,
    REPLAYED,
    REPLAY_FAILED
}