package com.example.kafka.demo.controller;

import com.example.kafka.demo.dto.CreateOrderCommand;
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
            @RequestBody CreateOrderCommand command) {
        producer.send(command);

        return "Order command published";
    }
}
