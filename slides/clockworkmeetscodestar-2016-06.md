% Clockwork meets <br> Codestar at Wehkamp
% Casper Koning
% 21 June 2016

# Wehkamp
## No longer the old-fashioned, dull, catalogue
![](img/clockwork-meets-codestar/wehkamplabs.png){style="width: 80%"}

## Ambition to grow, a lot

- Platform that supports this ambition
    - Blaze
- Data driven website
    - Completely A/B tested
    - Continuous, automated, data pipeline

## Next-gen e-commerce platform
![](img/clockwork-meets-codestar/wehkamplabs2.png){style="width: 70%"}



# Blaze
## Goals
![](img/clockwork-meets-codestar/blaze.png){style="width: 75%; float: right"}

- Low coupling
- High Flexibility
- High cohesion
- Consistency
- Reactive, meaning:
    - Resilient
    - Elastic
    - Message-Driven
    - Responsive

<aside class="notes">
- Low coupling: prevent unnecessary dependencies.
- High Flexibility: enable rapid change
- High cohesion: do one thing and do it well, the single responsibility principle
- Consistency: things should generally be consistent to limit learning curves
- Reactive, meaning:
    - Resilient: the platform is self-healing and should recover from problems with as little manual intervention as possible
    - Elastic: scaling is built in and should happen automatically based on demand
    - Message-Driven: inter-service communication is always done in an asynchronous and non-blocking manner
    - Responsive: consistently fast responses, also in case of errors.
</aside>

## How?
- Microservice architecture
    - Best architecture to provide previous goals
- Servers in the cloud
    - On demand provisioning of new servers
- Services developed in Scala
    - Best fit for the relevant frameworks and tools that allow for a microservice architecture
- Dedicated DevOps teams for end-to-end functionality
    - Teams are fully responsible for their own products, and bear any consequences
    - Leads to high quality products, reliable releases, and the right products through fast experimentation

# Data Platform
## Team Magenta
Three core products:

- Data platform
- Recommendations
- Search

## Data platform
- Data provisioning for Data Science and Business Intelligence teams
    - Data pipeline: from new product to usable, measurable data
    - Cluster infrastructure for near real-time processing on large data
- Event tagging:
    - Google analytics
    - Divolte
<center>
![](img/clockwork-meets-codestar/kafka.png){style="width: 25%; padding-right: 50px"}
![](img/clockwork-meets-codestar/spark.png){style="width: 25%; padding-bottom: 50px"}
![](img/clockwork-meets-codestar/divolte.png){style="width: 25%; padding-left: 50px"}
</center>

## Recommendations
![TODO](img/clockwork-meets-codestar/recommendations-itemitem.png){style="width: 80%"}

## Recommendations: AB Testing
![](img/clockwork-meets-codestar/recommendations-ab.png){style="width: 60%"}

## Recommendations: AB Testing
![](img/clockwork-meets-codestar/ab-result.png){style="width: 80%"}

## Search
- Browse
- Regular search engine
- Didyoumean?
- Typeahead
- Visual search

## Search: Visual Search
![](img/clockwork-meets-codestar/visual-search.png){style="width: 80%"}