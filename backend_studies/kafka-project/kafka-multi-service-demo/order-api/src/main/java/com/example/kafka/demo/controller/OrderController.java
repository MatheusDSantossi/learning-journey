package com.example.kafka.demo.controller;

import java.util.UUID;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.demo.producer.OrderProducer;

import lombok.RequiredArgsConstructor;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
@RequestMapping("/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderProducer orderProducer;

    @PostMapping
    public ResponseEntity<Void> createOrder(
            @RequestBody CreateOrderCommand command,
            @RequestHeader(value = "X-Correlation-Id", required = false) String correlationId) {
        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString()
                : correlationId;

        log.info("Publishing CreaterOrderCommand with correlationId={}", finalCorrelationId);

        orderProducer.send(command, finalCorrelationId);

        return ResponseEntity.accepted().build();
    }
}
