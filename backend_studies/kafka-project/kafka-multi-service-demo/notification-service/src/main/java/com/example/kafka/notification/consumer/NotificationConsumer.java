package com.example.kafka.notification.consumer;

import java.util.UUID;

import com.example.kafka.notification.dto.PaymentApprovedEvent;
import com.example.kafka.notification.service.NotificationService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.slf4j.MDC;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class NotificationConsumer {
    private final NotificationService notificationService;

    @KafkaListener(topics = "payments.approved", groupId = "notification-group")
    public void consue(ConsumerRecord<String, PaymentApprovedEvent> record,
            @Header(value = "X-Correlation-Id", required = false) String correlationId,
            Acknowledgment acknowledgment) {
        String finalCorrelationId = (correlationId == null || correlationId.isBlank()) ? UUID.randomUUID().toString()
                : correlationId;

        log.info("notification-service received correlationId={}", finalCorrelationId);

        MDC.put("correlationId", finalCorrelationId);
        try {
            log.info("Recevied PaymentApprovedEvent");
            System.out.println("Received PaymentApproved event: ");
            System.out.println(record.value());

            notificationService.sendNotification(record.value());

            acknowledgment.acknowledge();
        } finally {
            MDC.remove("correlationId");
        }
    }
}
