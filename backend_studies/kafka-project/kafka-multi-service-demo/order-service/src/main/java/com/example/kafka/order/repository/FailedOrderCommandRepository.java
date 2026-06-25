package com.example.kafka.order.repository;

import com.example.kafka.order.entity.FailedOrderCommand;
import com.example.kafka.order.entity.FailedOrderCommandStatus;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;


public interface FailedOrderCommandRepository extends JpaRepository<FailedOrderCommand, Long>  {
    List<FailedOrderCommand> findByStatusOrderByFailedAtDesc(FailedOrderCommandStatus status);
}
