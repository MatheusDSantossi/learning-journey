package com.example.kafka.demo.controller;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import com.example.kafka.demo.producer.OrderProducer;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderProducer producer;

    @PostMapping
    public String createOrder(
            @RequestBody OrderCreatedEvent event) {
        producer.send(event);

        return "Order event published";
    }
}
