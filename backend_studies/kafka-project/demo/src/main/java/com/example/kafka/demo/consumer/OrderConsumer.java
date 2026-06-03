package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
public class OrderConsumer {
    @KafkaListener(topics = "orders", groupId = "order-group")
    public void consumer(ConsumerRecord<String, OrderCreatedEvent> record, Acknowledgment acknowledgment) {
        System.out.println("----- MESSAGE RECEIVED -----");
        System.out.println("Key: " + record.key());
        System.out.println("Partition: " + record.partition());
        System.out.println("Offset: " + record.offset());
        System.out.println("Value: " + record.value());

        System.out.println("record.value().getOrderId(): " + record.value().getOrderId());
        if ("ORD-2".equals(record.value().getOrderId())) {
            try {

                throw new RuntimeException("Simulated failure");
            } catch (RuntimeException error) {
                // Handle the exception
                System.out.println("Exception caught: " + error.getMessage());
            }
        }

        acknowledgment.acknowledge();
    }
}
