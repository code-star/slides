% GraphQL <br> for Microservices
% Hamza Haiken
  Ishan Sital
% 19 May 2016

# Who are we?

## Hamza

Dude from Switzerland who likes to code

- Started at Codestar in 2015
- Currently at Wehkamp, team <span style="background: white; color: #cc22ff; padding:5px; border-radius:3px; padding-bottom: 3px;">Purple</span> (CI/CD)
- Blog at [http://tenchi.team2xh.net](http://tenchi.team2xh.net)

## Ishan

- Started at Codestar in 2015
- Currently doing Scala at Wehkamp
    - Team <span style="color: lime; font-size: 1.1em">Lime </span>-- Wehkamp Universal App
        - back-end

<aside class="notes">
- Hi! My name is Ishaan. I've been with Codestar since the end of 2015 en on now on my first full-time Scala assignment at Wehkamp. Currently I'm in Team Lime, which is repsonsible for developing the back-end of the android and iOS mobile apps. In the second half of the presentation i'll give you a peek into how this works. But for now i'll give the word back to hamza to talk more about the Wehkamp and it's infrastructure.
</aside>

# Wehkamp ![](img/graphql/wehkamp.png){style="height:0.7em;margin-bottom:-0.05em"}

##

![](img/graphql/wehkamp_site.png){width="75%"}

##

![](img/graphql/wehkamp_mobile.png){style="height: 70vh;"}

##

- Switch from .NET monolith to Scala microservices (Blaze Architecture)
- Combination of products/software/applications that are made or bought
- Using the latest technologies
- Lots of fun!

## Teams

- Many teams, split in colors
- Each team responsible for their services:
    - Maintenance
    - Deployment
    - Monitoring
    - Alerting

## CI/CD

- The Blaze Architecture has a strong focus on automation → speed of execution
- Platform deployed using *Ansible*
- Builds done on Jenkins, with promotion pipelines and integrated testing
- All services in Docker containers
- Containers run on *Mesos*, managed by *Marathon*

## Microservices

- Flexible specification allows for polyglottism:
    - Mainly Scala
    - Node.js
    - .NET
- Metadata about services centralized in *Consul*
- All services expose a health check endpoint for *Marathon*
- All services expose *Prometheus* metrics, big focus on monitoring
- Centralized logging with *Elasticsearch*

## Architecture

![Simple diagram of the Blaze Architecture](img/graphql/blaze-simple.svg){width="70%"}

## Scala @ Wehkamp

- Main language for services
- Aligns with platform goals

 

- Most services are actor based using Akka
    - Easy to scale
    - Akka persistence & clustering
- Routing with Spray

# Situation

## 

![Before](img/graphql/situation_before.svg){width="60%"}

##

![Currently](img/graphql/situation_current.svg){width="40%"}

##

![What we need](img/graphql/situation_wanted.svg){width="65%"}

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

- Abstracts different services into one API
- Specification, not a framework

## Advantages

- Very flexible query language
- Has interesting features:
    - Query shaped like the expected data
    - Introspection
    - Strongly typed
    - Recursive queries
- Looks like JSON
- Reponses are valid JSON

## Facebook ![](img/graphql/facebook.svg){style="height:0.7em;margin-bottom:-0.05em; border: 2px solid white; border-radius: 3px;"}

- Started working on GraphQL in 2012
- Needed a "data-fetching API powerful enough <br> to describe *all of Facebook*" for their mobile app
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

## Blaze Architecture goals

- **Loosely coupled**: prevent unnecessary dependencies
- **Highly flexible**: enable rapid change
- **Consistent**
- **Resilient**
- **Elastic**: built-in scalability
- **Message-driven**
- **Responsive**

##

We find that GraphQL meets some of these goals quite well:

- **Flexible**: write the scheme once, build powerful queries
- **Consistent**: the scheme reflects the consistency of the services
- **Elastic**: no state, can scale by running multiple GraphQL servers
- **Resilient**: handles errors quite well. <br> Returns partial results when some services are unreachable

The only goal not met is the **loose coupling**, but:

- There's no current alternative, everyone has to produce a *mega*-schema

# Examples

## Case 1

Our app needs to retrieve the title of a product.

## Querying the product service

![Using no query service](img/graphql/case1_old.svg){width="75%"}

## 

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

![Using a query service](img/graphql/case1_new.svg){width="75%"}

##

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

##

![Using no query service](img/graphql/case2_old.svg){width="30%"}

##

![Using no query service](img/graphql/case2_new.svg){width="50%"}

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
- GrapiQL
- Introspection
</aside>

# Query service

##

Given all the goals cited earlier,

we set out to create a Query Service,

aimed at the mobile app (for now)

<aside class="notes">
- Give short summary of previously defined goals
- what are going to talk about now?
    - Architecture
    - Wiring it together with Scala
    - Demo
    - Alternatives
</aside>

## "BFF" Pattern

- "Backends For Frontends"
- Mobile App logic
- Named Queries

<aside class="notes">
- This kind of service is also called BFF: "Backends For Frontends"
    - what is it? A tightly coupled API geared to one specific client application
    - is also a microservice
- Used by many companies (term coined by Soundcloud)
- We do not want logic in apps
- Define different APIs for each *kind* of client
- We can do this with GraphQL named queries

</aside>

## Examples

Mobile BFF:

```
/mobile/product_title?id=ID
/mobile/recommendation_list?id=ID
...
```

Desktop BFF:

```
/desktop/product_informations?id=ID
/desktop/recommendation_tree?id=ID
...
```

<aside class="notes">
- How do you call this BFF?
- It's just an namespaced endpoint on our service
</aside>

## Microservice architecture

- Scattered data
- Network costs
- "BFF" fit
- Dual functionality:
    - Named Query BFF
    - Internal GraphQL endpoint
    
<aside class="notes">
- Data scattered across multiple services
- Internal hops have no cost
- "BFF" fits perfectly as an internal microservice
- Dual functionality:
    - Named query BFF for mobile clients
    - Internal GraphQL endpoint for internal services
</aside>

##

Raw GraphQL
```http
POST query-service.blaze/graphql HTTP/1.1
{
 product(748002) {
   title
 }
}
```

Named query BFF
```http
GET query-service.blaze/mobile/get_title?id=748002 HTTP/1.1
```

<aside class="notes">
- Both API calls give the same result
- 1. posts the query to be executed
- 2. gets defined the endpoint for the title
    - under water the graphql is executed to yield the same result
</aside>


## Query service architecture

- Two main routes using Spray
    - Named Queries BFF endpoint
    - Raw GraphQL endpoint

- Schema
- Resolvers
- Helpers

<aside class="notes">
- Two main routes using Spray
    - Raw GraphQL endpoint
    - Named queries
- Manual schema and resolver implementation
- Useful helpers reduce the length and redundancy of the code
- (Code will be shown later)
</aside>

## Sangria ![](img/graphql/sangria.svg){style="height:0.7em;margin-bottom:-0.05em"}

- Young library
- Scala alternatives?
- Up-to-date

<aside class="notes">
- When we started the POC, it was a bit cumbersome (needed lots of helper functions)
- Library is young, updates all the time
- Already way easier to use after a few updates
- No alternatives for Scala yet
- GraphQL spec is still in movement, but Sangria follows closely
</aside>

## Schema definition

- Map JSON responses from external services
- case classes
- Nesting
- Reference to other objects

```scala
case class Recommendation(score: Option[BigDecimal], product_number: Option[String]) {
  @GraphQLField
  def product(implicit ctx: Ctx): Remote[Product] = remote(product_number)
}
```

<aside class="notes">
- Reflects the JSON schema of REST API responses from external services
- Schema objects defined with Scala case classes
- Straight forward thanks to helpers and macros
- We add fields when objects need to be nested
- Object fields can refer to other objects of the schema

Code snippet Voice-Over
- Define an object to hold the responses we get from the Recommendation service
- case class just like a Java class, 2 parameters score and product_number, with type of Option[BigDecimal] and a Option[String]
- Annotation from Sangria to mark the accessor members of the case class, in this case Recommendation has a field "product"
- implicit is not important for this example, a context is provided
- This function returns a Remote[Product]
- It's implementation is simply calling the remote function with the product_number parameter.
</aside>
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

Then, Sangria needs to know how to convert <br> from `JsObject` to our case class `Recommendation`

```scala
private implicit val RecommendationFormat = jsonFormat2(Recommendation)
```

Those two lines are the only things we need to write <br> when we need to add a new service.

##

- Sangria needs a `TypedEntityResolver` class that knows where to get data
- The `resolveSingle()` method queries the correct service and returns a `JsObject`

```scala
case class GetSingleEntityResolver(serviceKey: String, path: String)
    extends TypedEntityResolver[JsObject, GetQuery] {

  def resolveSingle(args: GetQuery)
      (implicit ctx: GraphQlContext): Future[Option[JsObject]] = {
    val request = HttpRequest(
      HttpMethods.GET,
      replaceUriPlaceholders(Uri(ctx.services(serviceKey) + path), replace), 
      ...
    )
    ctx.sendReceive(request).map(parseJsonObject)
  }

  override def resolve(...) = items map { item ⇒ resolveSingle(item.args) }
}
```

##

- *Hard coupling* between the query service and other services
-  Also need to actively *maintain* a schema

Is it worth it? **Yes**:

- Merging services is done in a transparent way
- Coupling is not added, but moved
- The APIs don't change that much
- Schema easy to write and maintain
- Integration testing alerts from API changes

## Named queries

To avoid putting logic in apps, we can use named queries:

```php
query($product_numbers: [String!]!) {
  products(product_numbers: $product_numbers) {
    title
    properties {
      label
    }
  }
}
```

- Looks like a normal query, wrapped in a `query` object with parameters
- Stored in namespaces (one for each client BFF, for example `mobile`)

##

In our service, we store named queries in files, which has some advantages:

- They are validated at test time
- Easy to maintain a folder hierarchy
- Better for version control
- All named queries can be compiled at boot time to save resources

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

# Alternatives

##

Before jumping in with GraphQL, we also investigated:

![](img/graphql/finagle.png){style="height:4.95em;margin-bottom:-0.05em; border-radius: 5px;"} ![](img/graphql/falcor.svg){style="background: black; padding: 10px; border-radius: 5px; height:4.5em;margin-bottom:-0.05em"}

Both had more cons than pros compared to GraphQL


## GraphQL vs Finagle

- Merging services:
    - In GraphQL, you first set up the resolvers and Schema, <br>then you can combine multiple services at a whim with the powerful *query syntax*
    - In Finagle, you need to *explicitly* write "Proxies" <br> for *each combination* of services that you want to merge

## GraphQL vs Falcor

- GraphQL is a *specification*, with multiple implementations
- Falcor is a *JavaScript* server *application*

# Conclusion

## Results

- Less data used: between 10% and 20% of original response sizes
- Less connections: only one connection for everything
- Tailored responses: only get what was asked for


## Aftermath

- The mobile team is happy
- Current development app uses the new named queries
- Investment in the schema enables us to re-use it

<aside class="notes">
- named queries can be added easily. 
- Front-end centered, you ask from the service what you need
    - When data could not be queried, we need to add it to the schema once
    - after that we can reuse it
</aside>

## Future

- Automatic schema generation through documentation
- Add more BFFs 

<aside class="notes">
- use service descriptors to automatically create schema's, less work 
    - no know solutions yet
- connect website, TV apps, VR ? all get there on BFF
    
</aside>

# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>
