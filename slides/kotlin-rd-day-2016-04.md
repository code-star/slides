% Kotlin R&D day
% Hamza Haiken <span style='font-size: 25%;'>(who also made the tool, blame him for bugs)</sub>
  David Hoepelman
  Donovan de Kuiper
% 15 April 2016

# What is ![Kotlin](img/kotlin.png){width=70px} Kotlin

##

* New language by Jetbrains
* Meant to convert Java devs
* Design goals:
    * Concise 
    * Safe (Static typing, no nulls)
    * Versatile (JVM, Android, Browser)
    * Interoparable (with Java)

# Comparison to Scala

## Same

<ul style="font-size: 50%;">
<li>No-semicolons</li>
<li>Expression-based</li>
<li>Backpacks to escape keywords/spaces</li>
<li>Covariant/contravariant generics</li>
<li>Default arguments</li>
<li>Operator overloading</li>
<li>Unchecked exceptions (even from Java)</li>
<li>Companion objects</li>
<li>Type interference (local)</li>
<li>Override modifier</li>
<li>Constructor syntax `class Foo(arg: val)`, also fields.</li>
<li>Class iniatilization blocks (explicit)</li>
<li>Operators collection (`x[a] ==> x.get(a)`)</li>
<li>Apply method (`x() ==> x.invoke()`)</li>
<li>Multiple constructors have to call the primary</li>
<li>Algebraic Data Type / Sealed classes</li>
<li>Val/var immutable/mutable</li>
<li>Mutable and immutable classes</li>
<li>Range literals</li>
<li>Collections immutable by default</li>
<li>No multiple inheritance, ut with interface</li>
<li>Flatmap</li>
<li>Data class/case class (automatic equals/hascode etc.)</li>
<li>Static typing</li>
<li>Unit</li>
</ul>

## Different

* Override modifier even for interface/trait implementations
* Explicit return (unless `Unit`) 
* Classes and methods are sealed/final by default (same as C++, C#)
* `when` expressions instead of `switch` or `if-else` trees

```Kotlin
when(x) {
	1, 2 -> println("1 or 2")
	3 -> println("That's a 3")
	else -> println("TODO: add all other numbers")
}
```

## Different2

* No `new` keyword `val x = MyClass()`
* No fields, always properties (backing fields can be accessed if necessary)
* Far less generic

```
fun x() { 1 }
fun y(a: Int) { a }
x + 1            // Nope
x() + 1
(1..10).map(y)   // Nope
(1..10).map(::y)
```

* Lots of specialized keywords

## Keywords

<img style="display: block; width: 500px; float: right;" src="img/kotlinrd/keywordallthethings.jpg" />

* `operator`
* `vararg`
* `open`
* `internal`
* `data`
* `annotation`
* `tailrec`
* `inline`
* `infix`
* `companion`
* `...`

<br style="clear:both"/>

## Better

* Java Interop
* Java Enums
* Explicit inlining (scala 2.12 has some inlining)
* Extension methods

```Kotlin
infix fun Int.myFancyPlus(other : Int) {
	return this + other
}
1 myFancyPlus 2
```

## Better

* Null safety

```Kotlin
val x : Int  = null // Compile error
val y : Int? = null

val a = y.?call()   // Null propagation, a = null
val b = y ?: -1     // Elvis operator
val c = y!!.call()  // throws NPE if null
```

## Worse/missing

<img src="img/kotlinrd/yunopatternmatch.jpeg" width="240" style="display: block; float: right; margin-left: 50px; margin-top: 65px;" />

* Pattern matching

```
when(e) {
	Foo(1,2) -> // Works because Foo implements equals
	Foo(a,b) -> // Doesn't compile
}
val (a,b) = Foo(1,2) // "alternative"
```

<br style="clear:both"/>

## Worse / Missing

* Implicits, implicit conversions
* Macros
* Special characters in methods (`route ~ index`)
* Value types (planned)
* Type classes
* Traits (java 8 style interfaces instead)
* Lazy keyword
* For comprehensions

# Overview

##

Pro:

+ Good Java interop
+ Easy mixing Java and Kotlin
+ Easier transition from Java
+ Good IDE support
+ Small runtime

Cons: 

<ul class="minusbullets">
<li>Way less advanced than Scala</li>
<li>No ecosystem</li>
<li>You're stuck to Jetbrains/IntelliJ</li>
<li>Unknown long-term language viability</li>
</ul>

## 

<div style="height: 100px;"></div>

> if you are happy with Scala, you most likely do not need Kotlin

<center>-- Kotlin docs</center>

 
# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>