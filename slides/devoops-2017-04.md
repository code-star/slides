% A DEVOOPS STORY: <br> <small> Breaking your entire data platform with a minor version upgrade </small>

# About
![](img/devoops/codestar-logo.png){style="display: block; margin: auto; background:white; width:50%"}
</br>
![](img/devoops/wehkamp-logo.png){style="display: block; margin: auto; background:white; width:50%"}

# Dev at Wehkamp
## Overview
![](img/devoops/blaze-team-overview.png){style="display: block; margin: auto; width: 60%"}

## Blaze microservice platform
![](img/devoops/stack.png){style="display: block; margin: auto; width: 60%"}

## Data platform
![](img/devoops/data-platform.png){style="display: block; margin: auto; width: 60%"}

## Monitoring solutions
![](img/devoops/efk.png){style="width:30%"}
![](img/devoops/grafana.jpg){style="width:25%"}
![](img/devoops/prometheus.jpg){style="width:25%"}

## How it fits together:
![[Cockpit](http://url-on-a-private-network)](img/devoops/cockpit.png){style="width:65%"}

# The main character
## Kafka and the product-merge
![](img/devoops/product-merge.png){style="width:30%"}

## Kafka details
![](img/devoops/topic.png){style="float:right"}

- Topic
- Partitioning
- ISR
- Compaction

# A bug!
## Increased task durations
![](img/devoops/airflow.png){style="width:50%"}

## Tracking the issue -- Debugging Spark
![](img/devoops/spark.png){style="width: 85%"}

## Tracking the issue -- Checking Kafka
```
blaze-ansible queue-nodes -m raw -a "du -ch /services/kafka/completeProduct-*"

10.200.8.177 | SUCCESS | rc=0 >>
4.1G    /services/kafka/completeProduct-0
4.2G    /services/kafka/completeProduct-10
4.1G    /services/kafka/completeProduct-12
4.2G    /services/kafka/completeProduct-14
4.4G    /services/kafka/completeProduct-15
4.1G    /services/kafka/completeProduct-16
4.2G    /services/kafka/completeProduct-18
4.1G    /services/kafka/completeProduct-2
4.2G    /services/kafka/completeProduct-20
4.2G    /services/kafka/completeProduct-21
4.1G    /services/kafka/completeProduct-22
4.2G    /services/kafka/completeProduct-24
4.3G    /services/kafka/completeProduct-26
4.3G    /services/kafka/completeProduct-27
4.3G    /services/kafka/completeProduct-28
4.1G    /services/kafka/completeProduct-3
4.1G    /services/kafka/completeProduct-30
4.1G    /services/kafka/completeProduct-32
4.1G    /services/kafka/completeProduct-33
4.2G    /services/kafka/completeProduct-34
4.0G    /services/kafka/completeProduct-4
4.3G    /services/kafka/completeProduct-6
4.0G    /services/kafka/completeProduct-8
4.1G    /services/kafka/completeProduct-9
99G total

10.200.8.176 | SUCCESS | rc=0 >>
1.8G    /services/kafka/completeProduct-1
1.9G    /services/kafka/completeProduct-11
1.8G    /services/kafka/completeProduct-13
2.0G    /services/kafka/completeProduct-14
1.9G    /services/kafka/completeProduct-15
1.7G    /services/kafka/completeProduct-17
1.8G    /services/kafka/completeProduct-19
1.9G    /services/kafka/completeProduct-2
1.9G    /services/kafka/completeProduct-20
1.9G    /services/kafka/completeProduct-21
1.8G    /services/kafka/completeProduct-23
1.9G    /services/kafka/completeProduct-25
1.8G    /services/kafka/completeProduct-26
2.1G    /services/kafka/completeProduct-27
1.7G    /services/kafka/completeProduct-29
1.8G    /services/kafka/completeProduct-3
1.9G    /services/kafka/completeProduct-31
1.8G    /services/kafka/completeProduct-32
1.8G    /services/kafka/completeProduct-33
1.7G    /services/kafka/completeProduct-35
2.0G    /services/kafka/completeProduct-5
1.8G    /services/kafka/completeProduct-7
1.7G    /services/kafka/completeProduct-8
1.9G    /services/kafka/completeProduct-9
44G total

10.200.8.183 | SUCCESS | rc=0 >>
3.1G    /services/kafka/completeProduct-0
78M /services/kafka/completeProduct-1
3.2G    /services/kafka/completeProduct-10
286M    /services/kafka/completeProduct-11
3.1G    /services/kafka/completeProduct-12
271M    /services/kafka/completeProduct-13
3.1G    /services/kafka/completeProduct-16
118M    /services/kafka/completeProduct-17
3.2G    /services/kafka/completeProduct-18
146M    /services/kafka/completeProduct-19
3.1G    /services/kafka/completeProduct-22
270M    /services/kafka/completeProduct-23
3.2G    /services/kafka/completeProduct-24
137M    /services/kafka/completeProduct-25
3.3G    /services/kafka/completeProduct-28
100M    /services/kafka/completeProduct-29
3.1G    /services/kafka/completeProduct-30
109M    /services/kafka/completeProduct-31
3.2G    /services/kafka/completeProduct-34
167M    /services/kafka/completeProduct-35
3.0G    /services/kafka/completeProduct-4
197M    /services/kafka/completeProduct-5
3.3G    /services/kafka/completeProduct-6
114M    /services/kafka/completeProduct-7
40G total
```

## Finding the root cause
```bash
ssh root@<kafka-ip>
cat /services/log/kafka/log-cleaner.log | grep ERROR | less
```
Revealed that we were dealing with broken log compaction [KAFKA-4497](https://issues.apache.org/jira/browse/KAFKA-4497)

## Time for an upgrade
KAFKA-4497 is fixed in the new Kafka (minor) version 0.10.1.1

# Disaster strikes
## A wild sold-out product appears!
![](img/devoops/orders2.png){style="width:60%"}

## Devops tries to diagnose
![](img/devoops/effective.png)

## Devops settles for a workaround
![](img/devoops/confusion.jpg)

## Devops settles for a workaround
![](img/devoops/always-publish.png){style="width:50%"}

# The Resolution
## Diagnosing the problem
```bash
ssh root@<kafka-broker-ip>
cat /services/log/kafka/server.log | grep ERROR | less

[2017-04-03 14:16:36,003] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3734742 for partition [completeProduct,13] out of range; reset offset to 3179215 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:36,367] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3688796 for partition [completeProduct,11] out of range; reset offset to 3139765 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:36,786] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3628910 for partition [completeProduct,17] out of range; reset offset to 3098787 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:37,093] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3633348 for partition [completeProduct,1] out of range; reset offset to 3082086 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:37,481] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3706480 for partition [completeProduct,7] out of range; reset offset to 3156826 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:37,785] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3703053 for partition [completeProduct,5] out of range; reset offset to 3142527 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:38,091] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3619023 for partition [completeProduct,35] out of range; reset offset to 3086012 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:38,416] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3714348 for partition [completeProduct,31] out of range; reset offset to 3153547 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:38,752] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3642120 for partition [completeProduct,29] out of range; reset offset to 3103819 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:38,810] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3693406 for partition [completeProduct,19] out of range; reset offset to 3156618 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:39,030] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3625320 for partition [completeProduct,25] out of range; reset offset to 3065658 (kafka.server.ReplicaFetcherThread)
[2017-04-03 14:16:39,360] ERROR [ReplicaFetcherThread-0-180881591], Current offset 3698289 for partition [completeProduct,23] out of range; reset offset to 3150514 (kafka.server.ReplicaFetcherThread)
```

## Adding dashboards
![](img/devoops/grafana.png)

## Adding alerts
![](img/devoops/alert.png){style="width:75%"}

## Fixing logs
![](img/devoops/logs.png){style="width:75%"}

# Takeaway points
