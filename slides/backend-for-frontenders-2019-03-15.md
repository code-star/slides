% Backend for </br>Frontenders (BFF)
% Ishan Sital
% 15 March 2019

# Disclaimer
- Brownbag
- Front-end developers

<aside class="notes">
As this is a "Brownbag" This talk will be a short introduction into some common technologies and frameworks used by our Codestar colleagues at clients. I'll try to keep it at 20 minutes with some time in the end for questions and discussion. 
</aside>

# Buzzwords
![](http://www.scala-lang.org/resources/img/scala-logo-red.png), FRP, Play, Akka, Streaming, Kafka, Docker, Kubernetes, CI/CD

<aside class="notes">
As a front-end developer you might have heard common "buzzwords" fly around the office. Some come up more often than not, and that's probably because we as Codestar have decided to use these frameworks because of there advantages. I'll to give an overview of some of the technologies used by Codestar.
</aside>

# Codestar

## Building
> Data-Intensive Reactive Applications

## What is Reactive?
>Reactive means reacting to changes in a timely manner or responding to changes in a timely manner.

- Here, in the Reactive World, we can represent a change as an *event*.
- Reactive programming is a kind of programming paradigm to that propagates changes.

## Functional Programming
- Pure functions
- Immutable data
- Expressions `<->` statements
- Composability
    - Higher Order Functions or combinators

```scala
map, flatMap, filter, reduce, fold
```

<aside class="notes">
As we use pure functions and immutable data to write our applications, we will get lots of benefits for free. For instance, with immutable data, we do not need to worry about:
- shared-mutable states,
- side effects,
- and thread-safety.
</aside>

## Functional Reactive Programming (FRP)
Use benefits of RP and FP

### RP
- Asynchronous 
- Non-blocking

### FP
- Pure function
- Immutability
- Combinators

# Scala

## What is it?
- SCalable LAnguage
-   a programming language
- Lightbend
- Multi-paradigm
    - Functional 
    - OO
- Strongly Typed

## loose comparison
- Lodash
- RxJS
- TypeScript
- JVM `<->` Browser
```bash
npx create-react-app my-ts-app --typescript
...
npm build
```
```bash
sbt new playframework/play-scala-seed.g8
...
sbt assembly
```

## Why should you care?
- Backend Frameworks
    - Play
    - Akka HTTP

# Backend

## Comparison
![Akka HTTP VS Play Framework](img/bff/audi-dtm-VS-regular-a5-1.jpg)

## Akka
- Foundation of Play, Akka HTTP et al.
- Actor Model
- State
- Message

> Akka is a toolkit for building highly concurrent, distributed, and resilient message-driven applications for Java and Scala

# Streaming

## Real-Time
> Would you cross the street with <br/>information that is 5 min old?

## Frameworks
- Kafka
- Akka Streams

## Kafka
![](img/bff/Kafka-Cluster-Diagram.png)

# Big Data

## Spark
- Memory
- Reduce problem

# Running

## Packaging
- Docker

## Deploying
- Docker
- Kubernetes

## Where?
- Cloud
    - Heroku
    - AWS
    - Google Cloud Platform
    - Azure
    - Bluemix

# CI / CD
- Git
- Bamboo
- CircleCI
- Travis


# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>
