package com.example.kafka.order.consumer;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.service.OrderService;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
public class CreateOrderCommandConsumer {
    private final OrderService orderService;

    public CreateOrderCommandConsumer(OrderService orderService) {
        this.orderService = orderService;
    }

    @KafkaListener(topics = "orders.commands", groupId = "order-service-group")
    public void consume(ConsumerRecord<String, CreateOrderCommand> record, Acknowledment acknowledgment) {
        System.out.println("Received CreateOrderCommand: " + record.value());

        orderService.handle(record.value());

        acknowledgment.acknowledge();
    }
}
