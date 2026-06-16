package com.example.kafka.payment.dto;

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

    public String getOrderId() {
        return orderId;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public String getPaymentId() {
        return paymentId;
    }

    public void setPaymentId(String paymentId) {
        this.paymentId = paymentId;
    }

    public String getApprovedAt() {
        return approvedAt;
    }

    public void setApprovedAt(String approvedAt) {
        this.approvedAt = approvedAt;
    }

    @Override
    public String toString() {
        return "PaymentApprovedEvent{" +
                "orderId='" + orderId + '\'' +
                ", paymentId='" + paymentId + '\'' +
                ", approvedAt=" + approvedAt +
                '}';
    }
}
