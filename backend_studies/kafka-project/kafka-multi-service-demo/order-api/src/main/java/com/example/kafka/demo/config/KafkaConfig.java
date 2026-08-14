package com.example.kafka.demo.config;

import com.example.kafka.demo.dto.CreateOrderCommand;
import org.springframework.kafka.listener.ContainerProperties;
import org.apache.kafka.common.TopicPartition;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.core.ConsumerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.listener.DefaultErrorHandler;
import org.springframework.kafka.listener.DeadLetterPublishingRecoverer;
import org.springframework.util.backoff.FixedBackOff;

@Configuration
public class KafkaConfig {
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> dltKafkaListenerContainerFactory(
            ConsumerFactory<String, CreateOrderCommand> consumerFactory,
            KafkaTemplate<String, CreateOrderCommand> kafkaTemplate) {

        ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> factory = new ConcurrentKafkaListenerContainerFactory<>();

        factory.setConsumerFactory(consumerFactory);
        factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL);

        DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(
                kafkaTemplate, (record, ex) -> new TopicPartition(record.topic() + ".DLT", record.partition()));

        DefaultErrorHandler errorHandler = new DefaultErrorHandler(
                recoverer,
                new FixedBackOff(1000L, 3L));

        factory.setCommonErrorHandler(errorHandler);

        return factory;
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> factKafkaListenerContainerFactory(
            ConsumerFactory<String, CreateOrderCommand> consumerFactory) {
        ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> factory = new ConcurrentKafkaListenerContainerFactory<>();

        factory.setConsumerFactory(consumerFactory);
        factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL);

        return factory;
    }
}
