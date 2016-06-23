% Clockwork meets <br> Codestar at Wehkamp
% Casper Koning
% 23 June 2016

# Wehkamp
## No longer the old-fashioned, dull, catalogue
![](img/clockwork-meets-codestar/wehkamplabs.png){style="width: 80%"}

## Ambition to grow, a lot
- E-Commerce is extremely competitive
- Need to develop features fast
- Need to be able to scale
- Platform that supports this ambition
    - Blaze
- Data driven website
    - Completely A/B tested
    - Continuous, automated, data pipeline

## Next-gen e-commerce platform
![](img/clockwork-meets-codestar/wehkamplabs2.png){style="width: 70%"}

# Blaze
## Goals
- Little to no coupling between services to allow for quick asynchronous development of new features
- Resilient to failure, because a single failing component should not prevent a user from having a nice shopping experience
- Elastic: scale out to more or fewer servers as demand dictates

![](img/clockwork-meets-codestar/blaze.png){style="width: 75%"}

## How?
- Microservice architecture
- Servers in the cloud
- Services developed in Scala
- Dedicated DevOps teams for end-to-end functionality
    - Teams are fully responsible for their own products, and bear any consequences
    - Leads to high quality products, reliable releases, and the right products through fast experimentation

# Team Magenta
## Data Engineering

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
![](img/clockwork-meets-codestar/divolte.png){style="width: 25%; padding-left: 50px; padding-bottom: 25px"}
</center>

## Recommendations
![](img/clockwork-meets-codestar/recommendations.png){style="width: 80%"}

## Recommendations: AB Testing
![](img/clockwork-meets-codestar/recommendations-ab.png){style="width: 60%"}

## Legacy
![](img/clockwork-meets-codestar/legacy.png){style="width:80%"}

## Recommendations: AB Testing
![](img/clockwork-meets-codestar/ab-result.png){style="width: 80%"}

## Search
![](img/clockwork-meets-codestar/visual-search.png){style="width: 50%; float: right"}

- Browse
- Regular search engine
- Didyoumean?
- Typeahead
- Visual search