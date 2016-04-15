% Slides Demo
% H. "Tenchi" Haiken
% 11 April 2016

# Showtime

## Introduction

- Python program made by yours truly
- Produces quality web pages for slide presentations
- Lots of scripting, testing and CSS-ing, so you don't have to

## Motivation

- Text is awesome
- Markdown is awesome
    - Decouple content from format
    - Can format and export content in many ways
- Alternatives are not
- Same slide-shows for the whole team, gives a structured image
- Self-hosted centralized "slides central"
- Version control, thanks to GitHub Pages
- Everyone can follow the slides from their machine, because it's just a web page

##

- Saves you a lot of time
    - Hello **Markdown** and modern features made for coders!
    - No need to fiddle with your mouse, moving around boxes in PowerPoint
    - Good bye ugly Google Docs templates
- You can check out the slides everywhere
- Nice features, thanks to:
    - Pandoc
    - MathJax
    - reveal.js

## Requirements

- [Pandoc](http://pandoc.org/) -- If you're on OS X: `brew install pandoc`
- [Click](http://click.pocoo.org/5/) -- With pip: `pip install click`
- [Watchdog](https://github.com/gorakhargosh/watchdog) -- With pip: `pip install watchdog`

## Usage

```plain
$ ./showtime.py --help
Usage: showtime.py [OPTIONS] COMMAND [ARGS]...

  It's Showtime! This tool helps you create awesome slides for your talks.

Options:
  --help  Show this message and exit.

Commands:
  build  Builds pages for given Markdown slides files.
  index  Generates an index page listing all slides.
  new    Generates a new set of slides for the given title.
  watch  Watch slides files for changes.
```

## Creating new slides

```bash
$ ./showtime.py new 'Hello, my awesome slides!'
Created: slides/hello-my-awesome-slides-2016-04.md
```

- Creates a stub from a template for you
- Sanitizes the name and adds the date

## Building the slides

```plain
$ ./showtime.py build slides/*
```

More convenient:

```plain
$ ./showtime.py watch
```

## Deploying to GitHub pages

...

## 

<br><br><br><p class="big">Demo!</p>

# Slides sectioning

- Use Markdown headers `#` for top-level sections
- Sections in reveal.js are displayed as a vertical column of slides
- Use level two headers `##` for sub-sections
- Use a level two header with no title to extend a slide into two parts

```markdown
# Example section

This is a section

## Sub-section 1

This is the 1^st^ sub-section

## Sub-section 2

This is the 2^nd^ sub-section
```

# Example section

This is a section

## Sub-section 1

This is the 1^st^ sub-section

## Sub-section 2

This is the 2^nd^ sub-section

# Refresher

You already know Markdown -- but Pandoc adds many features you may not be familiar with.

Here's a quick refresher, which will also serve as demonstrating what it looks like in slides.

# Formatting

## Emphasis

Surrounding text with asterisks `*` or underscores `_` emphasizes text.

The effect depends on numbers:

- Single makes *italic*
- Double makes **bold**
- Triple makes both ***italic and bold***

## Strikeout

Surrounding text with double tildes `~~` ~~strikes it~~

## Superscript and subscript

Surround text with circumflexes `^` to make it superscript, or tildes `~` for subscript:

- I like drinking H~2~O
- 2^10^ is 1024

## Verbatim / inline code

Surround text with back-ticks `` ` `` to make it monospace.
It also escapes formatting characters.

- Use the `force()` function
- `*I am not bold*`

## Horizontal rules

To produce a horizontal rule, use three regular dashes or more on their own line: `---`

---

Useful to mark a separation between points.

## $\LaTeX$

Slides support sweet $\LaTeX$ via MathJax.

- Surround code with dollars `$` for inline math: $\int_0^\infty e^{-x^2} dx=\frac{\sqrt{\pi}}{2}$
- Surround code with double dollars `$$` for centered equations:

$$
   \frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} =
     1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
      {1+\frac{e^{-8\pi}} {1+\ldots} } } }
$$

## HTML

You can also of course use raw HTML if you really need it.

A useful raw HTML element is the `<kbd>` tag which is nicely styled: <kbd>Ctrl</kbd> + <kbd>C</kbd>

## Links & images

- Use the following syntax for [links](): `[TITLE](URL)`
- Prefixing with `!` produces an image: ![Python Power](https://www.python.org/static/img/python-logo@2x.png){height=40px style="margin-bottom: -10px"}
- A line that only has an image will also display its caption:

```markdown
![Here's a caption](http://www.scala-lang.org/resources/img/scala-logo-red@2x.png)
```

![Here's a caption](http://www.scala-lang.org/resources/img/scala-logo-red@2x.png)

# Blocks

## Block quotes

Prefixing paragraphs with a greater-than symbol `>` produces a quotation block:

> I knew then (in 1970) that a 4-kbyte minicomputer would cost as much as a house. So I reasoned that after college, I'd have to live cheaply in an apartment and put all my money into owning a computer.

<center>Steve Wozniak via the `fortune` UNIX command</center>

## Code blocks

Multiple syntaxes exist, but let's only choose one:

- Surround multiple lines with triple back-ticks `` ``` `` to format it as code
- You can avoid language detection by specifying the language just after the back-ticks

<pre class="plain">
  <code>```scala
def foo(bar: Int): Int = 2 * bar
```</code>
</pre>

This produces:

```scala
def foo(bar: Int): Int = 2 * bar 
```

## Line blocks

If you wish to preserve indentation while producing normal, non-monospace text,

Prefix every line of a block with vertical pipes `|`:

| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

## Definition lists

You can produce definition lists by following this structure:

```markdown
Term
: Definition
```

Term 1
: Definition 1

Term 2
: Definition 2
  
    Second paragraph of definition 2.

## Tables

[Multiple syntaxes exist](http://pandoc.org/README.html#tables) for producing tables.

Here's the one I like:

```markdown
Header 1     | Header 2     | Header 3
:------------|:------------:|------------:
 Foo         |     "Fou"    |        0.42
 Bar         |    "Barre"   |       13.37
 Baz         |    "Base"    |       10.00

: Table caption
```

The colons `:` in the line separating the headers from contents determine alignment

##

Looks cumbersome. But this is in fact the simplest syntax compared to the others.

Also, you don't even need to align anything. This is also valid:

```markdown
Header 1|Header 2|Header 3
:---|:--:|---:
Foo|"Fou"|0.42
Bar|"Barre"|13.37
Baz|"Base"|10.00
```

Aligning stuff will just make your plain text *enjoyably readable* without the need of compilation.

##

Here's what the earlier table looks like:

Header 1     | Header 2     | Header 3
:------------|:------------:|------------:
 Foo         |     "Fou"    |        0.42
 Bar         |    "Barre"   |       13.37
 Baz         |    "Base"    |       10.00

: Table caption

# Typography

## Pandoc smart punctuation

- Quotes outside of code blocks are oriented: "double quotes", 'single quotes'
- `--` becomes en-dashes -- while `---` becomes an em-dash --- nice!
- `...` becomes an ellipsis...
- Non-breaking spaces are added after some abbreviations like "Mr."

## Fira Code ligatures

The awesome font used for all monospace elements in these slides is [*Fira Code*](https://github.com/tonsky/FiraCode)

It is one of the only coding font that takes advantage of the OTF format's ligature abilities, producing neat symbols for certain combinations:

```plain
                      .= .- := =:=           <<- <-- <- <-> -> --> ->>
                   == != === !== =/=     <=< <<= <==    <=> => ==> =>> >=>
                <<< << <= <>  >= >> >>>      >>= >>- >-     -< -<< =<<
                       <| <|> |>                 <~~ <~ ~~~ ~> ~~>
                
                   ~= ~- -~ =~ ~@        <$ <$> $>      \\ \\\ {- -} // ///
                 ^= ?= /= /== |= ||=     <+ <+> +>         /* /** **/ */
                    ## ### ####          <* <*> *>     </ <!-- www  --> />
                  #{ #[ #( #? #_ #_(                   0xF  9:45  m-x *ptr
```

##

- Tools like `scalariform` replace multiple characters with single Unicode characters 
- Characters in a ligature are still *separate*, they just show as a unique glyph
- That leaves your source code intact and pristine.
- The font also supports Powerline characters, you should totally use it for coding
- Fight for the preservation of original source code! Death to intrusive code formatters!

```scala
/** Maps are easy to use in Scala. */
val colors = Map("red" -> 0xFF0000, ...,  "brown" -> 0x804000)
def main(args: Array[String]) {
  for (name <- args) println(
    colors.get(name) match {
      case Some(code) => name + " has code: " + code
      case None       => "Unknown color: " + name
    }
  )
}
```

# reveal.js

## Keyboard shortcuts

Key                         | Action
:--------------------------:|----------------------------------
<kbd>←</kbd> / <kbd>→</kbd> | Navigate sections
<kbd>↑</kbd> / <kbd>↓</kbd> | Navigate subsections
<kbd>Space</kbd>            | Next **slide** (reverse with <kbd>Shift</kbd>)
<kbd>S</kbd>                | Open *speaker notes* window
<kbd>B</kbd> / <kbd>.</kbd> | Turn screen black
<kbd>F</kbd>                | Toggle fullscreen
<kbd>O</kbd>                | Toggle overview
<kbd>Esc</kbd>              | Exit fullscreen / toggle overview

## Speaker notes

Opens a separate window that shows you a bunch of nice informations:

- Elapsed time, current time
- Current and next slide
- Speaker notes

You can add speaker notes to slides like this:

```html
<aside class="notes">
Don't forget to talk about **speaker notes**:

- Uses `<aside>` tag
- Supports markdown formatting (speakers also need beautiful text)
</aside>
```

<aside class="notes">
Don't forget to talk about **speaker notes**:

- Uses `<aside>` tag
- Supports markdown formatting (speakers also need beautiful text)
</aside>

## Blackout

- Useful if you need to do something on a white/black board in front of the projector
- Or for a break

## Overview

- See everything at a glance
- You can quickly navigate to a subsection

## Slides scale

Using clever CSS zooming and scaling tricks,

reveal.js will make sure that your slides are *always* showing the same in every resolution.

- The virtual resolution chosen for the slides is 1280 by 720
- Slides have the exact same alignment of content for any screen aspect ratio

# Questions

##

<p class="huge">?</p>

##

<br><br><br><p class="big">Thank you</p>
