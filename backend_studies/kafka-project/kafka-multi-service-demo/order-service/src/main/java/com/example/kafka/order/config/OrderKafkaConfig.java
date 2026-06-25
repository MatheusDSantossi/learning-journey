package com.example.kafka.order.config;

import com.example.kafka.order.dto.CreateOrderCommand;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.TopicPartition;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.core.*;
import org.springframework.kafka.listener.ContainerProperties;
import org.springframework.kafka.listener.DefaultErrorHandler;
import org.springframework.kafka.listener.DeadLetterPublishingRecoverer;
import org.springframework.util.backoff.FixedBackOff;
import org.springframework.kafka.support.serializer.JsonDeserializer;

import java.util.HashMap;
import java.util.Map;

@Configuration
@EnableKafka
public class OrderKafkaConfig {
        @Bean
        public ConsumerFactory<String, CreateOrderCommand> consumerFactory() {
                Map<String, Object> props = new HashMap<>();

                props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
                props.put(ConsumerConfig.GROUP_ID_CONFIG, "order-service-group");
                props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
                props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);
                props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
                                org.apache.kafka.common.serialization.StringDeserializer.class);
                props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
                                org.springframework.kafka.support.serializer.JsonDeserializer.class);

                JsonDeserializer<CreateOrderCommand> deserializer = new JsonDeserializer<>(CreateOrderCommand.class,
                                false);
                deserializer.addTrustedPackages("com.example.kafka.order.dto");
                deserializer.setUseTypeHeaders(false);

                return new DefaultKafkaConsumerFactory<>(
                                props,
                                new org.apache.kafka.common.serialization.StringDeserializer(),
                                deserializer);
        }

        @Bean
        public ProducerFactory<String, Object> producerFactory() {
                Map<String, Object> props = new HashMap<>();

                props.put(org.apache.kafka.clients.producer.ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
                props.put(org.apache.kafka.clients.producer.ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
                                org.apache.kafka.common.serialization.StringSerializer.class);
                props.put(org.apache.kafka.clients.producer.ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
                                org.springframework.kafka.support.serializer.JsonSerializer.class);

                return new DefaultKafkaProducerFactory<>(props);
        }

        @Bean
        public KafkaTemplate<String, Object> kafkaTemplate() {
                return new KafkaTemplate<>(producerFactory());
        }

        @Bean(name = "kafkaListenerContainerFactory")
        public ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> kafkaListenerContainerFactory(
                        ConsumerFactory<String, CreateOrderCommand> consumerFactory,
                        KafkaTemplate<String, Object> kafkaTemplate) {

                ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> factory = new ConcurrentKafkaListenerContainerFactory<>();

                factory.setConsumerFactory(consumerFactory);

                DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(
                                kafkaTemplate,
                                (record, ex) -> new TopicPartition("orders.commands.DLT", record.partition()));

                DefaultErrorHandler errorHandler = new DefaultErrorHandler(
                                recoverer,
                                new FixedBackOff(1000L, 3L));

                factory.setCommonErrorHandler(errorHandler);
                factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL);

                return factory;

        }

        @Bean(name = "dltKafkaListenerContainerFactory")
        public ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> dltKafkaListenerContainerFactory(
                        ConsumerFactory<String, CreateOrderCommand> consumerFactory) {

                ConcurrentKafkaListenerContainerFactory<String, CreateOrderCommand> factory = new ConcurrentKafkaListenerContainerFactory<>();

                factory.setConsumerFactory(consumerFactory);
                factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL);

                return factory;
        }

}