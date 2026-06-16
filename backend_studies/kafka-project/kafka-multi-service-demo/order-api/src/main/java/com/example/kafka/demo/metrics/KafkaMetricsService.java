package com.example.kafka.demo.metrics;

import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Timer;
import org.springframework.stereotype.Component;

@Component
public class KafkaMetricsService {
    private final MeterRegistry meterRegistry;

    private final Counter orderProcessedCounter;
    private final Counter orderDuplicateCounter;
    private final Counter orderFailedCounter;

    private final Counter dltStoredCounter;
    private final Counter dltReplayedCounter;
    private final Counter dltReplayFailedCounter;

    private final Timer orderProcessingTimer;
    private final Timer dltReplayTimer;

    public KafkaMetricsService(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;

        this.orderProcessedCounter = Counter.builder("kafka.orders.processed")
                .description("Number of orders successfully saved").register(meterRegistry);

        this.orderDuplicateCounter = Counter.builder("kafka.orders.duplicates")
                .description("Number of duplicate orders ignored").register(meterRegistry);

        this.orderFailedCounter = Counter.builder("kafka.orders.failed")
                .description("Number of order processing failures").register(meterRegistry);

        this.dltStoredCounter = Counter.builder("kafka.dlt.stored").description("Number of failed events stored in DLT")
                .register(meterRegistry);

        this.dltReplayedCounter = Counter.builder("kafka.dlt.replayed")
                .description("number of DLT events replayed successfully").register(meterRegistry);

        this.dltReplayFailedCounter = Counter.builder("kafka.dlt.replay.failed")
                .description("Number of DLT replay failures").register(meterRegistry);

        this.orderProcessingTimer = Timer.builder("kafka.orders.processing.time")
                .description("Time spent processing OrderCreated events").register(meterRegistry);

        this.dltReplayTimer = Timer.builder("kafka.dlt.replay.time")
                .description("Time spent replaying dead-letter events").register(meterRegistry);
    }

    public Timer.Sample startOrderProcessingTimer() {
        return Timer.start(meterRegistry);
    }

    public Timer.Sample startDltReplayTimer() {
        return Timer.start(meterRegistry);
    }

    public Timer orderProcessingTimer() {
        return orderProcessingTimer;
    }

    public Timer dltReplayTimer() {
        return dltReplayTimer;
    }

    public void incrementOrderProcessed() {
        orderProcessedCounter.increment();
    }

    public void incrementOrderDuplicate() {
        orderDuplicateCounter.increment();
    }

    public void incrementOrderFailed() {
        orderFailedCounter.increment();
    }

    public void incrementDltStored() {
        dltStoredCounter.increment();
    }

    public void incrementDltReplayed() {
        dltReplayedCounter.increment();
    }

    public void incrementDltReplayFailed() {
        dltReplayFailedCounter.increment();
    }
}
