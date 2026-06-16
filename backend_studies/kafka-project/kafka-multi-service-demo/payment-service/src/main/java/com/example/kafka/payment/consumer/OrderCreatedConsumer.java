package com.example.kafka.payment.consumer;

import com.example.kafka.payment.dto.OrderCreatedEvent;
import com.example.kafka.payment.service.PaymentService;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
public class OrderCreatedConsumer {
    private final PaymentService paymentService;

    public OrderCreatedConsumer(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @KafkaListener(topics = "orders.created", groupId = "payment-group")
    public void consume(ConsumerRecord<String, OrderCreatedEvent> record, Acknowledgment acknowledgment) {
        OrderCreatedEvent event = record.value();

        System.out.println("Received OrderCreated event: " + event);

        paymentService.process(event);

        acknowledgment.acknowledge();
    }
}
