package com.example.kafka.notification.dto;

public class PaymentApprovedEvent {
    private String orderId;
    private String paymentId;
    private String approvedAt;

    public PaymentApprovedEvent() {

    }

    public PaymentApprovedEvent(String orderId, String paymentId, String approvedAt) {
        this.orderId = orderId;
        this.paymentId = paymentId;
        this.approvedAt = approvedAt;
    }

    // getters/setters

    public String getOrderId() {
        return orderId;
    }

    public String getPaymentId() {
        return paymentId;
    }

    public String getApprovedAt() {
        return approvedAt;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public void setPaymentId(String paymentId) {
        this.paymentId = paymentId;
    }

    public void setApprovedAt(String approvedAt) {
        this.approvedAt = approvedAt;
    }

    @Override
    public String toString() {
        return "PaymentApprovedEvent{" +
                "orderId='" + orderId + '\'' +
                ", paymentId='" + paymentId + '\'' +
                ", approvedAt='" + approvedAt + '\'' +
                '}';
    }
}
