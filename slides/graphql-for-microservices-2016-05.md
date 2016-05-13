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
+ Resilient

Cons: 

<ul class="minusbullets">
<li>Need to build a schema by hand</li>
<li>Non-trivial resolver implementation</li>
</ul>

<aside class="notes">
- Resilient: partial results when down, with error detail
</aside>

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

## Scala @ Wehkamp

- Main language for services
- Most services are actor based using Akka
    - Easy to scale
    - Akka clustering
- Routing with Spray

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

We need the recommendations for a certain product number,<br>
and for each we want the title and image.

For 10 recommendations, we would need to:

- Query the recommendations service
- Parse the response
- For each parsed product number:
    - Query the product service
    - Parse the response

## Merging services

<div style="float: left; width: 50%">
```scala
{
  recommendations(product_number: "748002") {
    products {
      product {
        title
        primary_image {
          file_name
        }
      }
    }
  }
}
```
</div>

<div style="float: right; width: 50%">
```json
{
  "data": {
    "recommendations": {
      "products": [
        {
          "product": {
            "title": "Apple iPad mini met Retina Display 16GB Wi-Fi",
            "primary_image": {
              "file_name": "114015_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "Tucano iPad Air 2 Filo folio hoes",
            "primary_image": {
              "file_name": "545728_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "Apple iPad Air met Retina Display 16GB Wi-Fi",
            "primary_image": {
              "file_name": "114718_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "Valenta iPhone 6 plus/ 6s plus flipcover",
            "primary_image": {
              "file_name": "489592_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "C&A Palomino sweater",
            "primary_image": {
              "file_name": "653834_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "C&A Palomino trui",
            "primary_image": {
              "file_name": "660709_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "C&A Palomino jurk",
            "primary_image": {
              "file_name": "691678_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "Melkco iPhone 6/6s Herman leren flipcover",
            "primary_image": {
              "file_name": "646375_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "C&A Palomino sweater",
            "primary_image": {
              "file_name": "674561_pb_01"
            }
          }
        },
        {
          "product": {
            "title": "C&A Palomino sweater",
            "primary_image": {
              "file_name": "626283_pb_01"
            }
          }
        }
      ]
    }
  }
}
```
</div>

##


Operation | Connections | Response length | Efficiency
:---------|------------:|----------------:|-----------:
Raw       |          11 |          ~14KiB |      3.48%
GraphQL   |           1 |           ~2KiB |     24.41%

: Effective size of useful/needed data: 500B <br> (10 products, titles and image names) <br><br>

## Case 3

For a given product, we need:

- Name
- Main picture
- 10 recommendations, and for each:
    - Name
    - Main picture
    - 10 recommendations, and for each:
        - Name
        - Main picture

## Recursion

<div style="float: left; width: 50%">
```scala
{
  product(product_number: "748002") {
    title
    primary_image { file_name }
    recommendations {
      products {
        product {
          title
          primary_image { file_name }
          recommendations {
            products {
              product {
                title
                primary_image { file_name }
              }
            }
          }
        }
      } 
    }
  }
}
```
</div>

<div style="float: right; width: 50%">
```json
{
  "data": {
    "product": {
      "title": "Apple  Ipad mini Smart Cover",
      "primary_image": {
        "file_name": "748002_pb_01"
      },
      "recommendations": {
        "products": [
          ...
        ]
      }
    }
  }
}
```
</div>

##

Operation | Connections | Response length | Efficiency
:---------|------------:|----------------:|-----------:
Raw       |         122 |         ~155KiB |       3.2%
GraphQL   |           1 |          ~29KiB |      17.2%

: Effective size of useful/needed data: ~5KiB <br> (111 products, titles and image names) <br><br>

# Demo 1

<aside class="notes">
We need to demo:

- Introspection
</aside>

# Query service

##

Given all the goals cited earlier,

we set out to create a query service,

aimed at the mobile app (for now)

## "BFF" Pattern

- This kind of service is also called BFF: "Backends For Frontends"
- Used by many companies (term coined by Soundcloud)
- We do not want logic in apps
- Define different APIs for each *kind* of client
- We can do this with GraphQL named queries

## Microservice architecture

- Data scattered across multiple services
- Internal hops negligible
- "BFF" fits perfectly as an internal microservice
- Dual functionality:
    - Named query BFF for mobile clients
    - Internal GraphQL endpoint for internal services

## Query service architecture

- Actor based using default actors from Blaze libraries
- Two main routes using Spray
    - Raw GraphQL endpoint
    - Named queries
- Useful helpers reduce the length and redundancy of the code
- Manual schema and resolver implementation

## Scala

*what do we use in the service?*

## Sangria

*how nice is sangria to use?*
*how does it compare to other implementatoins in other languages*

## Schema definition

- Schema objects defined with case classes
- Straight forward thanks to helpers and macros
- Reflects the JSON schema of REST API responses from services
- We add fields when objects need to be nested
- Object fields can refer to other objects of the schema

```scala
case class Recommendation(score: Option[BigDecimal], product_number: Option[String]) {
  @GraphQLField
  def product(implicit ctx: Ctx): Remote[Product] = remote(product_number)
}
```

##

We gain *flexibility* by merging services, but we introduce a *hard coupling* between the query service and other services. We also need to actively *maintain* a schema

Is it worth it? Yes:

- The APIs don't change that much
- Schema easy to write and maintain
- Integration testing alerts from API changes

## Resolver definition

First, we need to:

- Define which service needs to be called
- What is the REST endpoint (with placeholder variables)
- A magical helper function creates the resolver that:
    - Fetches the JSON
    - Parses and returns a `JsObject`

```scala
implicit val RecommendationsResolver: TypedEntityResolver[Recommendations, String] =
  getSingleEntityResolverId("recommendations-gateway", "/$id?panel=pdp_rec")
```

##

Then, Sangria needs to know how to convert from `JsObject` to our case class `Recommendation`

```scala
private implicit val RecommendationFormat = jsonFormat2(Recommendation)
```

Those two lines are the only things we need to write when we need to add a new service.

##

What does the resolver itself look like?

- Sangria needs a `TypedEntityResolver` class that knows where to get data
- The `resolveSingle()` method queries the correct service and returns a `Future` of `JsObject`

```scala
case class GetSingleEntityResolver
    (serviceKey: String, path: String, contentType: String)
    extends TypedEntityResolver[JsObject, GetQuery] {
  
  override def resolve(...): Vector[Future[Option[JsObject]]] =
    items map { item ⇒ resolveSingle(item.args) }

  def resolveSingle(args: GetQuery)
      (implicit ctx: GraphQlContext): Future[Option[JsObject]] = {
    
    val request = HttpRequest(
      HttpMethods.GET,
      replaceUriPlaceholders(Uri(ctx.services(serviceKey) + path), replace),
      ...
    )
    ctx.sendReceive(request).map(parseJsonObject)
  }
}
```

## Named queries

To avoid putting logic in apps, we can use named queries:

```plain
query($product_numbers: [String!]!) {
  products(product_numbers: $product_numbers) {
    title
    description
    properties {
      label
      value
    }
  }
}
```

- Looks like a normal query, wrapped in a `query` object with parameters
- We store named queries in namespaces (one for each client BFF, for example `mobile`)

##

In our service, we store named queries in files, which has some advantages:

- They are validated at test time
- Easy to maintain a folder hierarchy
- Better for version control

##

Before creating an endpoint for each named query, we need to parse them using Sangria:

```scala
val Success(queryAst) = QueryParser.parse(namedQuery.query)
```

We can then execute them (after injecting the correct parameters from the client request):

```scala
val userContext = GraphQlContext(executionContext, sendReceive, services, locale)
onComplete(executor.execute(queryAst, userContext, (), variables = jsonParams).mapTo[JsObject]) {
  case Success(response) ⇒
    processResponse(response)
  case _ => ???
}
```

## Security

- GraphQL only used internally, no outside access
- Public facing endpoint are named queries, which remove a lot of external control
- Public access still goes through the rest of the platform for other security checks

# Demo 2

<aside class="notes">

- Query service
    - Add named query (take query from Demo 1)
    - Named query example
- Bit of code
    - Schema
    - Resolvers
</aside>

# Results

- Less data used: between 10% and 20% of original response sizes
- Less connections: only one connection for everything
- Tailored responses: only get what was asked for

## Aftermath

- The mobile team is happy
- Current development app uses the new named queries
- Investment in the schema enables us to re-use it

## Future

- Automatic schema generation through documentation
- Add more BFFs

## 

# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>