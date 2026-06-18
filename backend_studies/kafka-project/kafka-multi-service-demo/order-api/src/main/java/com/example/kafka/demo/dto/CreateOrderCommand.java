package com.example.kafka.demo.dto;

public class CreateOrderCommand {
    private String orderId;
    private String customerId;
    private Double amount;

    public CreateOrderCommand() {}

    public CreateOrderCommand(String orderId, String customerId, Double amout) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.amount = amount;
    }

    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }

    public String getCustomerId() { return customerId; }
    public void setCustomerId(String customerId) { this.customerId = customerId; }

    public Double getAmount() { return amount; }
    public void setAmount(Double amount) { this.amount = amount; }
}
