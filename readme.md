# Showtime slides Generator

## Dependencies

```
$ brew install pandoc
$ pip install click watchdog
```

## Usage

```
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

## Controls

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

## Acknowledgements

- [Pandoc](http://pandoc.org/)
- [Click](http://click.pocoo.org/5/)
- [Watchdog](https://github.com/gorakhargosh/watchdog)
- [reveal.js](http://lab.hakim.se/reveal-js/)
- [highlight.js](https://highlightjs.org/)
- [`<kbd>` for Fun and Profit](https://kremalicious.com/using-kbd-for-fun-and-profit/)