package com.example.kafka.order.dto

public class CreateOrderCommand {
    private String orderId;
    private String customerId;
    private Double amount;

    public CreateOrderCommand() {}

    public CreateOrderCommand(String orderId, String customerId, Double amount) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.amount = amount;
    }

    public String getOrderId() { return orderId; }

    public void setOrderId(String orderId) { this.orderId = orderId;}

    public Double getAmount() { return amount; }
    public void setAmount(Double amount) { this.amount = amount;}

    @Override
    public String toString() {
        return "CreateOrderCommand{" +
                "orderId='" + orderId + '\'' +
                ", customerId='" + customerId + '\'' +
                ", amount=" + amount +
                '}';
    }

}
