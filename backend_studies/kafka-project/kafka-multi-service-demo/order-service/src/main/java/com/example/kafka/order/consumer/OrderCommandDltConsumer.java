package com.example.kafka.order.consumer;

import com.example.kafka.order.dto.CreateOrderCommand;
import com.example.kafka.order.service.FailedOrderCommandService;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.stereotype.Service;

@Service
public class OrderCommandDltConsumer {

    private final FailedOrderCommandService failedOrderCommandService;

    public OrderCommandDltConsumer(FailedOrderCommandService failedOrderCommandService) {
        this.failedOrderCommandService = failedOrderCommandService;
    }

    @KafkaListener(
        topics = "orders.commands.DLT",
        groupId = "order-command-dlt-group",
        containerFactory = "dltKafkaListenerContainerFactory"
    ) 
    public void consume( ConsumerRecord<String, CreateOrderCommand> record,
        @Header(name = KafkaHeaders.DLT_EXCEPTION_MESSAGE, required = false) String exceptionMessage,
        @Header(name = KafkaHeaders.DLT_ORIGINAL_TOPIC, required = false) String originalTopic,
        @Header(name = KafkaHeaders.DLT_ORIGINAL_PARTITION, required = false) Integer originalPartition,
        @Header(name = KafkaHeaders.DLT_ORIGINAL_OFFSET, required = false) Long originalOffset,
        Acknowledgment acknowledgment
    ) {
        failedOrderCommandService.storeFailedEvent(
            originalTopic,
            originalPartition,
            originalOffset,
            record.key(),
            record.value(),
            exceptionMessage
        );

        System.out.println("DLT RECEIVED -> " + record.value());

        acknowledgment.acknowledge();
    }
}
