package com.example.kafka.notification.consumer;

import com.example.kafka.notification.dto.PaymentApprovedEvent;
import com.example.kafka.notification.service.NotificationService;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
public class NotificationConsumer {
    private final NotificationService notificationService;

    public NotificationConsumer(NotificationService notificationService) {
        this.notificationService = notificationService;
    }

    @KafkaListener(
        topics = "payments.approved",
        groupId = "notification-group"
    )
    public void consue(ConsumerRecord<String, PaymentApprovedEvent> record, Acknowledgment acknowledgment) {
        System.out.println("Received PaymentApproved event: ");
        System.out.println(record.value());

        notificationService.sendNotification(record.value());

        acknowledgment.acknowledge();
    }
}
