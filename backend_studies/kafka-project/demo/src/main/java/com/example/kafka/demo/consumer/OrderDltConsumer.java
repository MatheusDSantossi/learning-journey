package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class OrderDltConsumer {
    @KafkaListener(topics = "orders.DLT", groupId = "order-dlt-group")
    public void consumeDlt(ConsumerRecord<String, OrderCreatedEvent> record) {
        System.out.println("----- DLT MESSAGE RECEIVED -------");
        System.out.println("Key: " + record.key());
        System.out.println("Partition: " + record.partition());
        System.out.println("Offset: " + record.offset());
        System.out.println("Value: " + record.value());
    }
}
