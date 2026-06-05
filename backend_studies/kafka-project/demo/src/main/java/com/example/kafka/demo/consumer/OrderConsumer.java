package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;

import java.util.HashSet;
import java.util.Set;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
public class OrderConsumer {
    private final Set<String> processedOrders = new HashSet<>();

    @KafkaListener(topics = "orders", groupId = "order-group")
    public void consume(ConsumerRecord<String, OrderCreatedEvent> record, Acknowledgment acknowledgment) {
        String orderId = record.value().getOrderId();

        if (processedOrders.contains(orderId)) {
            System.out.println(
                    "Duplicate message detected: " + orderId);

            acknowledgment.acknowledge();
            return;
        }

        if ("ORD-999".equals(orderId)) {
            throw new RuntimeException("Simulated crash");
        }

        processedOrders.add(orderId);

        // System.out.println("----- MESSAGE RECEIVED -----");
        // System.out.println("Key: " + record.key());
        // System.out.println("Partition: " + record.partition());
        // System.out.println("Offset: " + record.offset());
        // System.out.println("Value: " + record.value());

        // System.out.println("record.value().getOrderId(): " +
        // record.value().getOrderId());
        // if ("ORD-2".equals(record.value().getOrderId())) {
        // try {

        // throw new RuntimeException("Simulated failure");
        // } catch (RuntimeException error) {
        // // Handle the exception
        // System.out.println("Exception caught: " + error.getMessage());
        // }
        // }

        acknowledgment.acknowledge();
    }
}
