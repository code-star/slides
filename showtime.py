#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import click
import datetime
import glob
import os
import re
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


@click.group(help="It's Showtime! This tool helps you create awesome slides for your talks.")
def showtime():
    pass


@showtime.command(short_help="Builds pages for given Markdown slides files.")
@click.argument("files", nargs=-1, type=click.Path(exists=True))
def build(files):
    """
    Builds pages for given Markdown slides files.

    Accepts multiple files as argument. The index page will be generated automatically after this command is executed.
    """
    for file in files:
        build_file(file)
    generate_index()


@showtime.command(short_help="Generates a new set of slides for the given title.")
@click.argument("title")
def new(title):
    """
    Generates a new set of slides for the given title.

    A default template will be used, and the generated Markdown file will follow a naming convention.
    """
    now = datetime.datetime.now()
    sanitized = re.sub(r"[^(a-z0-9) ]", "", title.lower()).replace(" ", "-")
    destination = "slides/%s-%d-%02d.md" % (sanitized, now.year, now.month)

    with open("templates/slides.md", "r") as template_file:
        template = template_file.read()
        slides = template.format(
            title = title,
            destination = destination,
            date = now.strftime("%d %B %Y"),
        )
        with open(destination, "w") as output_file:
            output_file.write(slides)
            click.echo("Created: %s" % destination)


@showtime.command(short_help="Generates an index page listing all slides.")
def index():
    generate_index()


@showtime.command(short_help="Deploy slides to GitHub pages.")
def deploy():
    os.system("./deploy.sh")

@showtime.command(short_help="Watch slides files for changes.")
@click.option("-t", "--with-templates", is_flag=True, help="Also watch template files.")
def watch(with_templates):
    """
    Watch slides files for changes.

    Rebuilds files when changes have been detected.
    """
    event_handler = ShowtimeEventHandler()
    observer = Observer()

    observer.schedule(event_handler, "slides/")
    if with_templates:
        observer.schedule(event_handler, "templates/")


    observer.start()
    click.echo('Watching for changes in "slides/"%s...' % (' and "templates/page.html"' if with_templates else ""))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def generate_index():
    items = []
    for page in glob.glob("pages/*.html"):
        if page != "pages/index.html":
            with open(page, "rb") as html_file:
                html = html_file.read().decode("utf-8")
                title = re.search(r"(<title>)(.*?)(</title>)", html).group(2)
                year, month = page[:-5].split("-")[-2:]
                items.append((page[6:], year, month, title))

    with open("pages/index.html", "w") as output:
        w = output.write
        w("<h1>CODESTAR Slides</h1>\n")
        w("<ul>\n")
        for page, year, month, title in sorted(items, key=lambda t: t[1] + t[2]):
            w('  <li><a href="%s">[%s/%s] %s</a></li>\n' % (page, month, year, title))
        w("</ul>\n")


def build_file(file):
    with open(file, "rb") as f:
        basename = os.path.splitext(os.path.basename(file))[0]
        destination = "pages/%s.html" % basename
        updated = os.path.isfile(destination)

        pandoc_command = [
            "pandoc", file,
            "-t", "html5",
            "-f", "markdown+smart",
            "--template", "templates/page.html",
            "--standalone",
            "--mathjax",
            "--section-divs",
            "--no-highlight",
            "--variable", "theme=codestar",
            "--variable", "transition=linear",
            "--toc",
            "--toc-depth", "1",
            "-o", destination
        ]

        subprocess.call(pandoc_command)
        click.echo("%s: %s" % ("Updated" if updated else "Created", destination))


class ShowtimeEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        super(ShowtimeEventHandler, self).on_modified(event)

        what = "directory" if event.is_directory else "file"
        if what == "file":
            if event.src_path.startswith("templates/"):
                if event.src_path == "templates/page.html":
                    for file in glob.glob("slides/*.md"):
                        build_file(file)
                    generate_index()
            else:
                build_file(event.src_path)


if __name__ == "__main__":
    showtime()

