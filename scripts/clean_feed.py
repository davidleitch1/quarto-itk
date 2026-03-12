#!/usr/bin/env python3
"""Post-render script: remove items from posts.xml where the source .md has feed: false."""

import os
import re
import sys
import xml.etree.ElementTree as ET


def find_excluded_slugs(posts_dir):
    """Scan posts/*.md for YAML front matter containing feed: false.

    Returns a set of slugs (e.g. {'qld', 'test123'}) whose <link> should be
    stripped from the RSS feed.
    """
    excluded = set()
    feed_re = re.compile(r"^feed:\s*false\s*$", re.MULTILINE)

    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(posts_dir, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read(4096)  # front matter is always near the top
        except OSError:
            continue

        # Only look inside YAML front matter (between first two ---)
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        front_matter = parts[1]

        if feed_re.search(front_matter):
            slug = fname.removesuffix(".md")
            excluded.add(slug)

    return excluded


def clean_feed(project_dir):
    """Remove excluded items from _site/posts.xml. Returns number of items removed."""
    posts_dir = os.path.join(project_dir, "posts")
    feed_path = os.path.join(project_dir, "_site", "posts.xml")

    if not os.path.exists(feed_path):
        print("clean_feed: no _site/posts.xml found, skipping")
        return 0

    excluded = find_excluded_slugs(posts_dir)
    if not excluded:
        print("clean_feed: no posts with feed: false, skipping")
        return 0

    # Build suffix patterns like "posts/qld.html"
    patterns = {f"posts/{slug}.html" for slug in excluded}

    tree = ET.parse(feed_path)
    root = tree.getroot()

    # Find the <channel> element (direct child of <rss>)
    channel = root.find("channel")
    if channel is None:
        print("clean_feed: no <channel> element in RSS, skipping")
        return 0

    removed = 0
    for item in list(channel.findall("item")):
        link_el = item.find("link")
        if link_el is None or link_el.text is None:
            continue
        link_text = link_el.text.strip()
        if any(link_text.endswith(p) for p in patterns):
            channel.remove(item)
            removed += 1
            print(f"clean_feed: removed {link_text}")

    if removed:
        tree.write(feed_path, xml_declaration=True, encoding="UTF-8")
        print(f"clean_feed: wrote {feed_path} ({removed} item(s) removed)")

    return removed


if __name__ == "__main__":
    # Quarto sets cwd to the project directory when running post-render scripts
    project = os.getcwd()
    clean_feed(project)
