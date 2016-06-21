% Apache Spark
% Casper Koning
% May 2016

# Introduction
## What is Apache Spark?
> Apache Spark™ is a fast and general engine for large-scale data processing.

<center>![](img/spark-training/spark-stack.png){style="width: 60%"}</center>

## Why Apache Spark?
- Cluster processing on commodity hardware embracing failure
- Great performance due to in memory processing
- Easy to use
- Rich set higher-level tools for data analysis/processing

<center>![Logistic regression in Hadoop and Spark](img/spark-training/logistic-regression.png){style="width: 30%"}</center>

## How Apache Spark?
- First party support for multiple programming languages:
    - Scala (Spark source is also written in Scala)
    - Java
    - Python
    - R
- Integrates with Hadoop ecosystem via YARN
- Has Mesos interopt
- Can also be ran standalone

# Spark Core
## Spark architecture model

<center>![](img/spark-training/spark-architecture.png){style="width: 75%"}</center>

## The Spark Context
The first thing a Spark program must do is to create a SparkContext object, which tells Spark how to access a cluster, and functions as the gateway between the driver and the cluster.

```scala
val sparkConf = new SparkConf().setAppName("hello-spark").setMaster(master)
val sc = new SparkContext(sparkConf)
```
- Only one `SparkContext` may be active per JVM. You must `stop()` the active `SparkContext` before creating a new one
- The `master` is a Spark, Mesos, YARN cluster URL
- Setting `master="local"` runs in pseudo cluster mode


## RDDs
>A Resilient distributed dataset (RDD), is a fault-tolerant collection of elements that can be operated on in parallel.

```
val dataList = List(1,2,3,4,5)          //On driver
val dataRDD  = sc.parallelize(dataList) //Parallelized over cluster
```

## Creating RDDs
```scala
val fromCollectionOnDriver = sc.parallelize(List(1,2,3))
val fromLocalFileSystem = sc.textFile("/directory/*.txt")
val fromHdfs = sc.textFile("hdfs:///directory/*.txt")
val fromS3 = sc.textFile("s3a:///bucket/directory/*.txt")
val wholeTextFiles = sc.wholeTextFiles("/directory/*.txt")  // returned as filename-file key-value pairs
val customInputFormat = sc.newAPIHadoopRDD[K, V, F <: InputFormat[K, V]](...)
```

## Transformations and Actions
> RDDs support two types of operations: transformations, which create a new RDD from an existing one, and actions, which return a value to the driver after running a computation on the RDD.

- [transformations](http://spark.apache.org/docs/latest/programming-guide.html#transformations) are lazy
- [actions](http://spark.apache.org/docs/latest/programming-guide.html) force computation
- A pipeline of transformations and actions form a DAG

## DAG
<center>![](img/spark-training/spark-dag.png){style="width: 60%"}</center>

## Example
```scala
val rdd = sc.textFile("/this-training.md")
val rddCount = rdd.flatMap(line => line.split("\\s"))
   .map(word => word.toLowerCase)
   .filter(word => word == "rdd" || word == "rdds")
   .count()
println("I keep nagging about RDDs in this presentation, to be precise, " +
  "I mention them " + rddCount + " times")
```

## Clusterstuff: Fault tolerance
TODO

## Clusterstuff: Executors

## Clusterstuff: Workers
TODO

## Clusterstuff: Resource Negotiation
TODO

## Clusterstuff: Cluster mode vs Client mode
TODO

## Tasks, Jobs, and Stages
TODO

## Caching
Sometimes you want to reuse an RDD. By default, this leads to a recomputation of the RDD. This is where caching comes in.
```scala
val rdd = sc.textFile("/path")
val nextRDD = rdd.map(line => line.toLowerCase)
nextRDD.cache()
println(nextRDD.filter(line => line.startsWith("a")).count())
println(nextRDD.filter(line => line.startsWith("b")).count())
```

## Broadcasts/Accumulators
- Broadcast variable: read-only variable cached on each machine
- Accumulator: Write only variable, which can be updated with associative operations, and queried on the driver

```scala
val broadcastVar = sc.broadcast(1)
val accumulatorVar = sc.accumulator(0, "count")
val someRDD = sc. ...
someRDD.map(value => value.toInt + broadcastVar.value)
       .foreach(x => accumulatorVar += x)
println(accumulatorVar.value)
```

## Developing
- Prototype online with `spark-shell`
- Write production worthy code with tests, package to JAR and submit to cluster with `spark-submit`
- Notebooks, e.g. [spark-notebook](github.com/andypetrella/spark-notebook/blob/master/details.md), [Zeppelin](https://zeppelin.incubator.apache.org), [Databricks](https://databricks.com/product/databricks)
- Drag and drop tools  in development

## Testing
Holden Karau has an excellent tiny [library](https://github.com/holdenk/spark-testing-base) for testing Spark applications.
Most notably, this provides a `SharedSparkContext` trait which you can mix in with your test to provide an embedded Spark instance:
```scala
class SampleTest extends FunSuite with SharedSparkContext {
  test("test initializing spark context") {
    val list = List(1, 2, 3, 4)
    val rdd = sc.parallelize(list)

    assert(rdd.count === list.length)
  }
}
```

## CODE TIME
- Start up your `spark-shell`, and prototype your way to a working Spark program:
    - Provided is a file containing all works of Shakespeare (`shakespeare.txt`)
    - Perform a word count on the texts, i.e. for every unique word, provide a count of how many times it occurs
    - How many words are used only once?
    - Which word is used most?
    - Try leaving out whitespace and the license, how should you approach this?
- Migrate working pieces of code to a Spark program in your IDE ([template project](https://github.com/CasperKoning/spark-template))
- Assemble your JAR, `sbt clean assembly`
- Submit your JAR to a local pseudocluster using `spark-submit`


# Spark Streaming
## Architecture
<center>![streaming-arch](img/spark-training/streaming-arch.png){style="background: white; width: 60%"}</center>
<center>![streaming-flow](img/spark-training/streaming-flow.png){style="background: white; width: 60%"}</center>

## DStream
> *DStream* is the basic abstraction provided by Spark Streaming. It represents a *continuous
stream* of data [...] Internally, a DStream is represented by a *continuous series of RDDs*.

## Example
```scala
val ssc = new StreamingContext(sc, Seconds(2))
val dstream = ssc.socketTextStream("localhost",1234)

dstream
  .map(line => toRelevantEntity(line))
  .filter(entity => entity.isUseful())
  .foreachRDD{rdd =>
    rdd.foreach(entity => entity.executeSuperImportantSideEffect())
  }

ssc.start()
ssc.awaitTermination()
ssc.stop()
```

## Operations on DStreams [docs](http://spark.apache.org/docs/latest/streaming-programming-guide.html#window-operations)
When working with DStreams, you construct a pipeline of actions/transformations on the underlying RDDs of the stream.

<center>![streaming-dstream-ops](img/spark-training/streaming-dstream-ops.png){style="background: white;"}</center>

## Windowing operations on DStreams [docs](http://spark.apache.org/docs/latest/streaming-programming-guide.html#window-operations)
<center>![streaming-dstream-window](img/spark-training/streaming-dstream-window.png){style="background: white; width: 60%"}</center>

- Window length: The duration of the window.
- Sliding interval: The interval at which the window operation is performed.
- These two parameters must be multiples of the batch interval.

## Output operations on DStreams [docs](http://spark.apache.org/docs/latest/streaming-programming-guide.html#output-operations-on-dstreams)
<center>![rtfm](img/spark-training/rtfm.jpg)</center>

## Receivers
> Every input DStream (except file stream) is associated with a <strong>Receiver</strong> object which receives the data from a source and stores it in Spark’s memory for processing.

## Basic Sources
- Socket Streams
- File Streams
- Custom Actor Streams
- Queue RDD Streams (testing)

```scala
ssc.socketTextStream(host,port)
ssc.fileStream[KeyClass, ValueClass, InputFormatClass](dataDir)
ssc.actorStream(actorProps, actor-name)
ssc.queueStream(queueOfRDDs)
```

## Advanced Sources
- Kafka: spark-streaming-kafka
- Flume: spark-streaming-flume
- Kinesis: spark-streaming-kinesis
- Twitter: spark-streaming-twitter
- ZeroMQ: spark-streaming-zeromq
- MQTT: spark-streaming-mqtt

Require linking with external libs, include in Uberjar

## Custom Sources
```scala
class MyReceiver(storageLevel: StorageLevel) extends NetworkReceiver[String](storageLevel) {
    def onStart() {
    // Setup stuff (start threads, open sockets, etc.)
    // Must start new thread to receive data, as onStart() must be
    // non-blocking.
    // Call store(...) in those threads to store received data into
    // Spark's memory.
    // Call stop(...), restart(...) or reportError(...) on any thread
    // based on how different errors needs to be handled.
    }

    def onStop() {
    // Cleanup stuff (stop threads, close sockets, etc.) to stop
    // receiving data.
    }
}
```

## Fault tolerance
> A streaming application must operate 24/7 and hence must be resilient to failures unrelated to the application logic. For this to be possible, Spark Streaming needs to *checkpoint* enough information to a fault- tolerant storage system such that it can recover from failures.

## Checkpointing
- Metadata Checkpointing
     - Configuration
     - DStream operations
     - Incomplete batches
- Data Checkpointing
     - Saving of the generated RDDs to reliable storage [...] intermediate RDDs of stateful transformations are periodically checkpointed to reliable storage to cut off the dependency chains.

## Turning on checkpointing
```scala
def functionToCreateCtxt(): StreamingContext = {
    val ssc = new StreamingContext(...)   // new context
    val lines = ssc.socketTextStream(...) // create DStreams
    ...
    ssc.checkpoint(checkpointDir)   // set checkpoint directory
    ssc
}

val context = StreamingContext.getOrCreate(checkpointDir, functionToCreateCtxt _)
context. ...
context.start()
context.awaitTermination()
```
Create DStreams inside the method: [SPARK-13316](https://issues.apache.org/jira/browse/SPARK-13316)

## CODE TIME
Set up a simple Spark Streaming program.
```scala
$ spark-shell
val ssc = new StreamingContext(sc, Seconds(2))
val dstream = ssc.socketTextStream("localhost",1234)
...
ssc.start()
ssc.awaitTermination()
ssc.stop()
```
Linux/OSX: Use Netcat, `nc`, to send data:
```bash
nc -lk 1234
hello world
```

<!-- Windows: Use Telnet, `telnet`, or download a Netcat alternative, to send data:
```batch
telnet localhost 1234
hello world
``` -->

# Spark SQL

## Overview
> Spark SQL is a Spark module for structured data processing. [...] The interfaces provided by Spark SQL provide Spark with more information about the structure of both the data and the computation being performed. Internally, Spark SQL uses this extra information to perform extra optimizations.

<center>![spark-sql-architecture](img/spark-training/spark-sql-architecture.png){style="background: white; width: 90%;"}</center>

## Dataframe
> A DataFrame is a distributed collection of data organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood.

## Example
```scala
val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

val df = sqlContext.read.json("/some_path/people.json")
df.show()
df.printSchema()
df.select("name").show()
df.select(df("name"), df("age") + 1).show()
df.select($"name", $"age" + 1).show()
df.filter(df("age") > 21).show()
df.groupBy("age").count().show()
df.select(avg("age")).show()
```

## Spark SQL operations
- [DataFrame docs](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrame), for operations on DataFrames
- [org.apache.spark.sql.functions](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions), for operations on Columns</li>
- SQL queries for registered tables: `val df = sqlContext.sql("SELECT * FROM table")`

## Loading and Saving data
1. Default format is parquet
2. Can be configured:

    ```scala
    df.read.format("json").load("input_directory/file.json")
    df.write.format("json").save("output_directory/file.json")
    ```

3. Also supports JDBC

    ```scala
    val jdbcDF = sqlContext.read.format("jdbc").options(
            Map("url" -> "jdbc:postgresql:dbserver",
              "dbtable" -> "schema.tablename")
          ).load()
    ```

4. Out of the box Hive with HQL via own DSL
5. Other datasources via third party plugins

## Dataset
> A Dataset is a new experimental interface added in Spark 1.6 that tries to provide the benefits of RDDs (strong typing, ability to use powerful lambda functions) with the benefits of Spark SQL’s optimized execution engine.

## CODE TIME
Start your spark shell with an aditional package for reading CSV:
```bash
spark-shell --packages com.databricks:spark-csv_2.10:1.4.0
```

- Some JSON with data on persons is provided. Load in this data, and print its schema
- Select the persons who are active and older than 21, and print only their name and address
- Count the number of persons without friends. For the ones that do have friends, print their names, and their friends
- Some CSV is provided with hashes belonging to each person, indexed by `_id`. Load in this data and join it with the previous data
- Write the result as CSV to disk


# Spark MLlib
## Machine Learning Basics
![Typical steps in a machine learning pipeline](img/spark-training/machineLearningPipeline.png)


## Gather and prepare data
> In Data Science, 80% of time is spent on data preparation, and the other 20% is spent on complaining about the need to prepare data.

## Select features
> In machine learning and statistics, feature selection, also known as variable selection, attribute selection or variable subset selection, is the process of selecting a subset of relevant features (variables, predictors) for use in model construction

- Current age for predicting the probability of ending up in hospital in the coming five years.
- $\frac{\text{weight}}{\text{length}^2}$ for predicting percentage of body fat.
- You fall in category $A$, so you are very likely to do $Z$.

## Train a model
![Model examples](img/spark-training/modelgraphs1.png){style="float:left;  width: 60%"}
![Iris decision tree](img/spark-training/J48_iris.jpg){style="float:right;  width: 35%"}

## Select the best model
- Train model with different parameters, compare with some metric
- Model might be too complex, or too simple
- Evaluate model on some validation set and use cross-validation to find an appropriate model

![Model selection](img/spark-training/model-selection.png)
<!-- FIXME Put image to the right of the text FIXME-->

## Predict
![](img/spark-training/xkcdFlowChart.png)

## MLlib Programming absractions
- (Dense/Sparse) Vector
- LabeledPoint
- Matrix
- Rating
- Model classes
- Pipeline API

## (Dense/Sparse) Vector
- A mathematical vector containing numbers
- Both dense and sparse vectors
- Constructed via `mllib.linalg.Vectors`
- Do not provide arithmetic operations

```scala
val denseVec1 = Vectors.dense(1.0, 2.0, 3.0)
val denseVec2 = Vectors.dense(Array(1.0,2.0,3.0))
val sparseVec = Vectors.sparse(4, Array(0,2), Array(1.0, 2.0))
```

## LabeledPoint
> LabeledPoint: A labeled data point for supervised learning algorithms such as classification and regression. Includes a feature vector and a label.

```scala
val lp = LabeledPoint(1,Vectors.dense(3.14,1.68,1.41))
```

## Matrix
- Integer typed row and column indices
- Double values
- Different implementations for distribution purposes (RowMatrix, BlockMatric, CoordinateMatrix, ...)
- Dense and sparse variants

![](img/spark-training/latex_matrix.png)

## Rating
> Rating: A rating of a product by a user, used in the `mllib.recommendation` package for product recommendation.

Nothing more than a
```scala
case class Rating(user: Long, item: Long, rating: Double)
```

## Model classes
- Work on RDD[Vector], RDD[LabeledPoint], etc.
- Often follow naming pattern: <problem>With<algorithm>, e.g. LinearRegressionWithSGD.
- Either the model follows a builder pattern and has a run() method, or it has static train() and predict() methods:

```scala
val points: RDD[LabeledPoint] = // ...
val lr = new LinearRegressionWithSGD()
  .setNumIterations(200)
  .setIntercept(true)
val model = lr.run(points)
```

```scala
val model = DecisionTree.trainClassifier(
  input = data,
  numClasses = 5,
  ...)
```

## Pipeline api
- Advanced API for chaining machine learning operations in one workflow
- Uses the more advanced DataFrame features compared to RDD's of simple MLlib abstractions
- Possible pipeline: Automated feature selection -> Model training -> Validation -> Model selection -> Prediction

![](img/spark-training/machineLearningPipeline.png){style="width: 50%"}

## CODE TIME
- 42,000 drawing of digits
- Given a drawing, predict the written digit
- Classification problem
- Use Decision Tree approach

<center>
![](img/spark-training/digitData.png){style="width: 300px"}
![](img/spark-training/digit.png){style="width: 265px"}
</center>

# Spark GraphX

## Fundamentals
> In the most common sense of the term, a graph is an ordered pair $G=(V,E)$ compromising a set $V$ of vertices together with a set $E$ of edges, which are 2-element subsets of $V$.

- Graphs are all about relationships between objects
- Vertices are the objects we ware interested in
- Edges describe the relationship between two vertices
- The alternate way of looking at data, allows us to ask different questions much easier. These questions are typically about relationships.

##

![](img/spark-training/graph.png){style="width: 50%;"}

## Programming abstractions in GraphX
```scala
class Graph[VD, ED]{
  val vertices: VertexRDD[VD]
  val edges: EdgeRDD[ED]
}
type VertexRDD[VD] = RDD[(VertexID, VD)]
type EdgeRDD[ED] = RDD[Edge[ED]]
type Edge[ED] = (VertexID, VertexID, ED)
type VertexID = Long
```

## EdgeTriplet
![](img/spark-training/triplet.png)

## Constructing a Graph
There are several options for creating a Graph in GraphX:

- `Graph.apply(vertices, edges)`
- `Graph.fromEdges()` or `Graph.fromEdgeTuples()`
- `GraphLoader.edgeListFile()`

## Example: Maven Dependencies
![[source](https://github.com/ogirardot/meta-deps)](img/spark-training/maven-deps-ni-labels.png){style="width: 40%"}

## Data
- Directed graph of Maven dependencies
- Data structure:

![](img/spark-training/maven-deps-data.png){style="width: 75%"}

##

![](img/spark-training/mavenEntry.png)

##

![](img/spark-training/rowToTuple.png)

##

![](img/spark-training/appendWithUniqueId.png)

##

![](img/spark-training/establishRelationships.png)

# ???

<br><br><br><p class="big">Thank you!!</p>
