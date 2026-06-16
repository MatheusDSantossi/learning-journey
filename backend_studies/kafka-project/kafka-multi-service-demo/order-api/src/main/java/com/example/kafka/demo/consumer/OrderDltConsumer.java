package com.example.kafka.demo.consumer;

import com.example.kafka.demo.dto.OrderCreatedEvent;
import com.example.kafka.demo.service.DeadLetterService;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.stereotype.Service;

@Service
public class OrderDltConsumer {
    private final DeadLetterService deadLetterService;

    public OrderDltConsumer(DeadLetterService deadLetterService) {
        this.deadLetterService = deadLetterService;
    }

    @KafkaListener(topics = "orders.DLT", groupId = "order-dlt-group", containerFactory = "dltKafkaListenerContainerFactory")
    public void consumeDlt(
            ConsumerRecord<String, OrderCreatedEvent> record,
            @Header(name = KafkaHeaders.DLT_EXCEPTION_MESSAGE, required = false) String exceptionMessage,
            @Header(name = KafkaHeaders.DLT_ORIGINAL_TOPIC, required = false) String originalTopic,
            @Header(name = KafkaHeaders.DLT_ORIGINAL_PARTITION, required = false) Integer originalPartition,
            @Header(name = KafkaHeaders.DLT_ORIGINAL_OFFSET, required = false) Long originalOffset,
            Acknowledgment acknowledgment) {

        // System.out.println("----- DLT MESSAGE RECEIVED -------");
        // System.out.println("Key: " + record.key());
        // System.out.println("Partition: " + record.partition());
        // System.out.println("Offset: " + record.offset());
        // System.out.println("Value: " + record.value());

        System.out.println("DLT consumer received: " + record.value());

        try {

            deadLetterService.storeFailedEvent(
                    originalTopic,
                    originalPartition,
                    originalOffset,
                    record.key(),
                    record.value(),
                    exceptionMessage);

            System.out.println("DLT saved successfully");

            acknowledgment.acknowledge();
        } catch (Exception e) {
            e.printStackTrace();
            throw e;
        }

    }
}
