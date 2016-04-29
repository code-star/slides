% GraphQL for Microservices
% H. Haiken
  I. Sital
% 19 May 2016

# Who are we?

## Hamza

Dude from Switzerland who likes to code

- Started at Ordina in 2015
- Currently at Wehkamp, team **<span style="color: #cc22ff;">Purple</span>** (CI/CD)
- Blog at http://tenchi.team2xh.net

## Ishan

- Started at Ordina in 2015
- Currently at Wehkamp, team **<span style="color: lime;">Lime</span>** (Mobile app)

# Situation

- Wehkamp is migrating to a microservices architecture
- Mobile app has a single access point <br> → doesn't translate well to a microservices architecture

![Simple diagram of the Blaze architecture](img/graphql/blaze-simple.svg)

# Goals

##

- Reduce number of connections / calls
    - Gives some slack to our Routers and Gateways
    - Reduces network load on client app
- Reduce amount of data transferred
- Avoid upstream long review process when model changes

##

Basically, we want to:

*Merge multiple services into one access point*

This left us investigating multiple solutions and we chose **GraphQL**

# GraphQL ![](img/graphql/graphql.svg){style="height:0.7em;margin-bottom:-0.05em"}

##

<br><br>

> GraphQL is a query language designed to build client applications by providing an intuitive and flexible syntax and system for describing their data requirements and interactions.

<center>*Facebook (http://facebook.github.io/graphql#sec-Overview)*</center> 


## What is it?

- Very flexible query language specification
- Has interesting features:
    - Query shaped like the expected data
    - Introspection
    - Strongly typed
    - Recursive queries
- Looks like JSON
- Reponses are valid JSON

## Facebook ![](img/graphql/facebook.svg){style="height:0.7em;margin-bottom:-0.05em; border: 2px solid white; border-radius: 3px;"}

- Started working on GraphQL in 2012
- Needed a "data-fetching API powerful enough to describe *all of Facebook*" for their mobile app
- Has to be easy to learn by product developers
- Used today in their apps and servers
- Open sourced RFC

## Features

Pros:

+ Flexibility
+ Recursive queries
+ Easy to use

Cons: 

<ul class="minusbullets">
<li>Need to build a schema by hand</li>
<li>Non-trivial resolver implementation</li>
</ul>

## Alternatives

Before jumping in with GraphQL, we also investigated:

- Finagle ![](img/graphql/finagle.png){style="height:0.7em;margin-bottom:-0.05em"}
- Falcor ![](img/graphql/falcor.svg){style="height:0.7em;margin-bottom:-0.05em"}

Both had more cons than pros compared to GraphQL

## GraphQL vs Finagle

- Merging services:
    - In GraphQL, you first set up the resolvers and Schema, <br>then you can combine multiple services at a whim with the powerful *query syntax*
    - In Finagle, you need to *explicitly* write "Proxies" <br> for *each combination* of services that you want to merge

## GraphQL vs Falcor

- GraphQL is a *specification*, with multiple implementations
- Falcor is a *JavaScript* server *application*

# Wehkamp ![](img/graphql/wehkamp.png){style="height:0.7em;margin-bottom:-0.05em"}

## 

- Big online retailer
- Switch from .NET monolith to Scala microservices
- Using the latest technologies
- Lots of fun!

## Teams

- Many teams, split in colors
- Each team responsible for their services:
    - Maintenance
    - Deployment
    - Monitoring
    - Alerting

## Blaze architecture

New platform for Wehkamp, based on a microservices architecture.

Goals:

- **Lowly coupled**: prevent unnecessary dependencies
- **Highly flexible**: enable rapid change
- **Consistent**
- **Resilient**
- **Elastic**: built-in scalability
- **Message-driven**
- **Responsive**

##

We find that GraphQL meets some of these goals quite well:

- Flexible: write the scheme once, build powerful queries
- Consistent: the scheme reflects the consistency of the services
- Elastic: no state, can scale by running multiple GraphQL servers
- Resilient: handles errors quite well. Returns partial results when some services are unreachable

The only goal not met is the *low coupling*, but:

- There's no current alternative, everyone has to produce a *mega*-schema

## CI/CD

- Blaze has a strong focus on automation
- Platform deployed using *Ansible*
- Builds done on Jenkins, with promotion pipelines and integrated testing
- All services in containers, deployed on *Mesos*

## Microservices

- Flexible specification allows for polyglottism:
    - Mainly Scala
    - Node.js
    - .NET
- Metadata about services centralized in *Consul*
- All services expose a health check endpoint for *Marathon*
- All services expose *Prometheus* metrics, big focus on monitoring
- Centralized logging with *Elasticsearch*

## Cool stuff

- Experimenting with new technologies:
    - GraphQL POC
    - Kamon metrics
    - Prometheus

# Examples

## Case 1

Our app needs to retrieve the title of a product.

## Querying the product service

```json
{
  "normalized_name": "apple-ipad-mini-smart-cover-roze-0885909632497",
  "description": "<p>...</p>",
  "published": true,
  "product_number": "748002",
  "product_type": "REGULAR",
  "properties": [{
    "label": "Type iPad accessoire",
    "value": "Hoes/cover",
    "code": "X51"
  }, ...],
  "alternate_urls": [{
    "culture": "nl-nl",
    "url": "http://www.wehkamp.nl/elektronica/ipad-tablets/ipad-hoesjes/apple-ipad-mini-smart-cover/C26_6F0_F2P_748002/"
  }],
  "package_contents": "- iPad mini Smart Cover<br />",
  "vas_references": [],
  "title": "Apple  Ipad mini Smart Cover",
  "images": [{
    "file_name": "748002_eb_01",
    "category": "eb"
  }, {
    "file_name": "748002_pb_01",
    "category": "pb"
  }, {
    "file_name": "748002_eb_02",
    "category": "eb"
  }],
  "ean": "0885909632497",
  "available_stock": 3,
  "variants": [{
    "size": {
      "code": "000",
      "label": "000",
      "is_default": false
    },
    "price": 3495,
    "scratch_price": 4195,
    "vat_code": "VB6",
    "stock_info": [{
      "from": 1,
      "to": 3,
      "availability": {
        "min_hours": 0
      },
      "per_appointment": false
    }],
    "vat_percentage": 2100,
    "original_price": 4195,
    "available_stock": 3,
    "shipping": {
      "costs": 0,
      "vat_code": "WB6",
      "vat_percentage": 2100
    }
  }]
}
```

Total response length: 1358B (1.326KiB)

## Only get what you ask for

<div style="float: left; width: 50%">
```json
{
 product(748002) {
   title
 }
}
```
</div>

<div style="float: right; width: 50%">
```json
{
 "product": {
   "title": "Apple  Ipad mini Smart Cover" 
 }
}
```
</div>

Total response length: 64B (0.0625KiB)

## Case 2

We need data from the product service and the catalog service.

## Merging services

DO A QUERY WITH A PRODUCT AND CATEGORY

<div style="float: left; width: 50%">
```json

```
</div>

<div style="float: right; width: 50%">
```json

```
</div>

## Case 3

We need to get the product informations of the recommendations of a given product.

## Recursion

DO IT

# Demo
<aside class="notes">
We need to demo:
- What we have now
    - Product service
    - Recommendation service
- Combine with GraphQL
- Introspection
- Bit of code
    - Resolvers
    - Schema
- Query service
    - Add named query
    - Named query example
</aside>

# Query service
## "BFF"
## Microservice architecture
## Scala
## Sangria
## Schema
## Resolvers
## Named queries
## Security
## Testing

# Results
## Less data used
## Less connections
## Tailored responses
## Aftermath
## Future

## 

# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>