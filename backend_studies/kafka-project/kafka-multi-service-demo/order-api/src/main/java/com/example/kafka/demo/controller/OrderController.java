package com.example.kafka.demo.controller;

import com.example.kafka.demo.dto.CreateOrderCommand;
import com.example.kafka.demo.producer.OrderProducer;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderProducer orderProducer;

    @PostMapping
    public String createOrder(
            @RequestBody CreateOrderCommand command,
            @RequestHeader(value = "X-Correlation-Id", required = false) String correlationId
        ) {
            String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString() : correlationId;

        orderProducer.send(command, finalCorrelationId);

        return ResponseEntity.accepeted().build();
    }
}
