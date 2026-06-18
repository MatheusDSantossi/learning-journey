package com.example.kafka.notification.service;

import com.example.kafka.notification.dto.PaymentApprovedEvent;
import org.springframework.stereotype.Service;

@Service
public class NotificationService {
    public void sendNotification(PaymentApprovedEvent event) {
        System.out.println("-----------------------------------");
        System.out.println("Sending email...");
        System.out.println("Order : " + event.getOrderId());
        System.out.println("Payment: " + event.getPaymentId());
        System.out.println("Notification sent successfully!");
        System.out.println("-----------------------------------");

    }
}
