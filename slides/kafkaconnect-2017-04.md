% Kafka Connect
% Casper Koning
% 11 April 2017

# Kafka Basics
![](img/kafka-connect/kafka-basics.png){style="width:50%; float:right"}

- Topic
- Broker
- Producer
- Consumer
- Partitioning

# Kafka Connect

## Why
![](img/kafka-connect/kafka-connect.png){style="background: white; width: 50%"}

## What
- General framework for creating 'Connectors', that can run on Kafka Connect 'Workers' which can export/import data from/to Kafka
- Many (supported) community implementations of specific Connectors

## How -- a general workflow
- Pick [an existing Connector](https://www.confluent.io/product/connectors/) that works for you and you use it
- Roll your own

![](img/kafka-connect/connect-workflow.png){style="width: 80%; background: white"}

## How -- Overview
- SourceConnector / SinkConnector
- SourceTask / SinkTask
- KeyConverter, ValueConverter
- Worker

![](img/kafka-connect/connector-model.png){style="background: white"}


## How -- Connector
- Defines configuration for Tasks to be executed

```Java
public Class<? extends Task> getTaskClass();

public List<Map<String, String>> getTaskConfigs(int maxTasks);

public void start(Map<String, String> props);

public void stop()
```


## How -- Task
```Java
public void start(Map<String, String> props);
// For SourceTask
public List<SourceRecord> poll() throws InterruptedException;
// For SinkTask
public void put(Collection<SinkRecord> records);
public void flush(Map<TopicPartition, Long> offsets);
```

![](img/kafka-connect/task.png){style="background: white; width: 50%"}

## How -- Converters
![](img/kafka-connect/converter-basics.png){style="background: white"}

Configured per Worker!

## How -- Worker
- Actually runs connectors, comes in two flavors
  - Standalone
  - Distributed

## Testing
- Unit tests tend to be quite minimal, as Kafka Connect is all about integration between systems
- E2E Integration test via standalone mode:

```
bin/connect-standalone <connect-worker.properties> <connector.properties>
```

## Deployment
- Make sure Connector classes are packaged and on Worker's Classpath
- Start up Worker

```
bin/connect-distributed <worker.properties>
```

- Start up specific Connectors via the REST interface:

## Deployment -- REST Interface
```bash
curl -X POST -H "Content-Type: application/json" \
     --data '{
       "name": "local-file-sink",
       "config": {
         "connector.class":"FileStreamSinkConnector",
         "tasks.max":"1",
         "file":"test.sink.txt",
         "topics":"connect-test"
         }
    }' \
    http://<kafkaConnectHost>:8083/connectors
```

see the rest of the API [here](http://docs.confluent.io/3.2.0/connect/restapi.html#connect-userguide-rest)
