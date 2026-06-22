package com.example.kafka.order.repository;

import com.example.kafka.order.entity.OrderEntity;
import org.springframework.data.jpa.repository.JpaRepository;

@Service
@RequiredArgsConstructor
public class OrderCreatedProducer {
    private final KafkaTemplate<String, OrderCreatedEvent> kafkaTemplate;

    public void send(OrderCreatedEvent event) {
        kafkaTemplate.send(
                "orders.created",
                event.getCustomerId(),
                event
        );

        System.out.println("Sent OrderCreatedEvent: " + event);
    }
}
