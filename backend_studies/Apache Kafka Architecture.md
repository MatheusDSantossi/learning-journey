# Apache Kafka Architecture

At its core, Apache Kafka is a distributed streaming platform designed to handle real-time data streams. Kafka is built around the concept of publishing and subscribing to data streams, where data is organised into topics and can be consumed by multiple subscribers.

## Core components of Kafka

[image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*97MxzCnTfASRCWWLOgla4A.png)

* Producers: The applications or processes which publishes message to the Kafka topic
* Consumers: The application or processes which consumes messages from the Kafka topic.
* Brokers: Acts like a buffer between producer and consumer. It is responsible for replication, durability and delivery guarantee.
* Topics: The topics are the entities which store the messages published to it.
* Partitions: Each topic is divided into multiple partitions, Kafka ensures that messages are never lost through partition replication once it's acknowledged.

## Why Kadfka uses File System?

Kafka leverages the modern operating system page cache optimisation where the data is kept in main memory (page cache) once read till it gets evicted (minor overhead). Kafka first writes to page cache and then dirty pages get written to the file system efficently.

The design choice was heavuky ubfkyebced by the disk seek performance improvement that we have seen in recent times.

## Why Kafka doesn’t use any In-Memory Data Structure or B-Tree structure like RDBMS

Kafka is built on top of JVM hence it makes sense to use any efficient In-Memory data structure. Kafka is designed to deal with high volume of data hence maintaining a large object pool in the available main memory would eventually turn into a bottleneck instead it's much better choice to store compact by structure.

It is understandably slower when we compare with B-Tree like structure. Kafka provides a feature where we can maintain the produced data as long as we want which is easier to accommodate with cheaper storage. Considering the fact that we performance of tree based structures are super linear, would degrade with higher volume whereas the file based implementation is volume agnostic.

## It’s generally acknowledged disk reads are slow. How Kafka is still so performant?

There were 4 steps:

1. The operating system reads data from the disk into page cache in kernel space.
2. The application reads the data from kernel space into a user-space buffer.
3. The application writes the data back into kernel space into a socket buffer.
4. The operating system copies the data from the socket buffer to the NIC buffer where it is sent over the network.

Modern O/S implements Zero-Copy optimisation which allows data to be transferred over network from NIC buffer, that gets the data directly from page cache, effectively reducing two hops in between.

Kafka assumes all the messages would eventually be consumed by one or more consumers. Upon first read of the message, it stays in page cache and any subsequent consumption happens from page cache without looking up to the disk. (Q: "How much data can be kept in page cache to serve all the consumers?" A: "This depends on number of factors. The data volume is largely determined by the available memory on the Kafka broker machine. Kafka itself does not directly control the page cache but leverages it.")

## Is there anything else Kafka team thought that would improve performance?

Message size is default to 1MB and anything beyond is considered as anti-pattern for Kafka. When we think of a real time data streaming pipeline more often the bottleneck is network bandwidth. Kafka addresses it through the usage of compression in bulk. Some of the compression mechanisms are GZip, Snappy and LZ4 etc.

Kafka use standardised binary message format which is understood by all the pieces of Kafka infrascrutcture (Broker, Producer and consumer)

Kafka uses RecordBatch interface which groups the messages together to reduce network roundtrip which effectively addresses small I/O problem.

## How Kafka ensures durability?

Kafka messages get pushed into topics. Each topics has multiple partitions. Each partions is replicated into topics has multiple servers to ensure durability. Out of all the instances, Kafka maintains one leader and rest replicas turn into followers. Leader ensures the data gets written to the follower's log file successfully, so that in case the current leader fails any of the follower can turn in to leader.

Kafka dynamically maintains a set of in-sync replicas (ISR) that are always in sync with the leader. Only mebers of this set are eligible for election as leader. A write to a Kafka partition is not considered committed until all in-sync replicas have received the write.

## Below are the  possible message delivery guarantees

* At most once: Messages may be lost but are never redelivered.
* At least once: Messages are never lost but may be redelivered.
* Exactly once: This is what people actually want, each message is delivered once and only once.

Kafka by default follows "At least once" policy but with co-ordination (additional implementation of something like 2-Phase commit) with consumer application we can achieve "Exactly Once" guarantees.

## How data is actually stored in file system?

The log file contains below information:

* BaseOffset: Offset of first message in the batch
* LastOffset: Offset of last message in the batch
* Count: Number of messages in the batch
* Position: Oisutuib of the batch in the file
* CreatedTime: Created time of last message in the batch
* Size: Size of the batch (in bytes)

The index file contains information related to mapping of relative offset to position in the log file. It contains below information:

* Offset: Relative offset of the message
* Position: Position in log file

Kafka uses index & log files to quickly extract the message for a given offset.

## How Kafka maintains the data for so long?

Kafka needs to retain messages and to do that it needs to optmise the storage. One of the optimisation technique is log compaction. Log compaction ensures that Kafka will alawys retain at least the last known value for each message key within the log of data for a single topic partition. (Q: "Does log compaction is active from the start or does it start in the middle?". A: It is active from beginning. The Log Cleaner Thread keeps checking and performs the compaction. Point to note is these are configurable. For more you can refer to this: [Design Compaction Config](https://kafka.apache.org/documentation/#design_compactionconfig)). The idea is to selectively remove records where we have amore recent update with the same primary key. Anytime there is a failure, system would be able to bring the last committed state back by reprocessing the messages from the log.

Log compaction is a mechanism to give finer-grained per-record retention, rather than the coarser-gained time-based retention.

It's worth noting that the compaction activity doesn't hcange the existing offset by adjusting for the detled records;

[image 2](https://miro.medium.com/v2/resize:fit:640/format:webp/)1*kCzkvrvT-A6xEgpf65RKzQ.png

## Why do consumers need to pull the data from Kafka broker?

* In a push-based system it's difficult to deal with diverse consumers because the broker would control the rate at which data is pushed.
* In a push system a consumer can get overwhelmed when its rate of consumption falls below he rate of production (similar to a denial of service attack).
* Pull-based system enables the consumer to catch up when it can, if it falls behind production. The consumer can indicate it is overwhelmed and catch up can be implemented with some kind of backoff protocol.
* Pull-based system enables aggresive batching of data sent to the consumer. In constrat, a push-based system must either send a request immediately or accumulate more data and then sends it later without knowledge of whether the downstream consumer will be able to process it immediately.

## Conclusion

Apache Kafka's internal architecture is a well-engineered system designed to handle real-time data streams at scale. Its core components work together to provide data durability, fault tolerance, scalability, and efficient data processing. Understaing Kafka's internals is essential for building robust, high-performance streaming applications and data pipelines in today's data-driven world. As Kafka continues to evolve, it reamins a fundamental tool for organisations dealing with large volumes of real-time data.

[Full post](https://medium.com/@sutanu3011/kafka-a-peek-into-internals-b47b9dc6fd0f)
