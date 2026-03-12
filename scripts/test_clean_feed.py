"""Tests for clean_feed post-render script."""

import os
import xml.etree.ElementTree as ET

import pytest

from clean_feed import clean_feed, find_excluded_slugs

SAMPLE_RSS = """\
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>ITK Research</title>
    <link>https://itkservices3.com</link>
    <item>
      <title>QLD Disaster Recovery</title>
      <link>https://itkservices3.com/posts/qld.html</link>
    </item>
    <item>
      <title>Longhaul Freight</title>
      <link>https://itkservices3.com/posts/Longhaul.html</link>
    </item>
    <item>
      <title>China Update</title>
      <link>https://itkservices3.com/posts/China_update.html</link>
    </item>
  </channel>
</rss>
"""


@pytest.fixture
def project(tmp_path):
    """Set up a minimal project directory with posts/ and _site/."""
    posts = tmp_path / "posts"
    posts.mkdir()
    site = tmp_path / "_site"
    site.mkdir()

    # Post WITH feed: false
    (posts / "qld.md").write_text(
        "---\ntitle: QLD\nfeed: false\ndraft: false\n---\nContent here\n"
    )
    # Posts WITHOUT feed: false
    (posts / "Longhaul.md").write_text(
        "---\ntitle: Longhaul\ndraft: false\n---\nContent here\n"
    )
    (posts / "China_update.md").write_text(
        "---\ntitle: China\nfeed: true\n---\nContent here\n"
    )

    # Write sample RSS
    (site / "posts.xml").write_text(SAMPLE_RSS)

    return tmp_path


def test_find_excluded_slugs(project):
    slugs = find_excluded_slugs(project / "posts")
    assert slugs == {"qld"}


def test_excluded_item_removed(project):
    removed = clean_feed(str(project))
    assert removed == 1

    tree = ET.parse(project / "_site" / "posts.xml")
    channel = tree.getroot().find("channel")
    links = [item.find("link").text for item in channel.findall("item")]

    assert "https://itkservices3.com/posts/qld.html" not in links
    assert "https://itkservices3.com/posts/Longhaul.html" in links
    assert "https://itkservices3.com/posts/China_update.html" in links


def test_remaining_items_intact(project):
    clean_feed(str(project))
    tree = ET.parse(project / "_site" / "posts.xml")
    channel = tree.getroot().find("channel")
    assert len(channel.findall("item")) == 2


def test_valid_rss_after_clean(project):
    clean_feed(str(project))
    tree = ET.parse(project / "_site" / "posts.xml")
    root = tree.getroot()
    assert root.tag == "rss"
    assert root.find("channel") is not None


def test_no_posts_xml(tmp_path):
    """Script exits cleanly when there is no posts.xml."""
    posts = tmp_path / "posts"
    posts.mkdir()
    (posts / "qld.md").write_text("---\nfeed: false\n---\n")
    # No _site directory at all
    removed = clean_feed(str(tmp_path))
    assert removed == 0


def test_no_excluded_posts(tmp_path):
    """XML is unchanged when no posts have feed: false."""
    posts = tmp_path / "posts"
    posts.mkdir()
    site = tmp_path / "_site"
    site.mkdir()

    (posts / "Longhaul.md").write_text("---\ntitle: Longhaul\n---\n")
    (site / "posts.xml").write_text(SAMPLE_RSS)

    removed = clean_feed(str(tmp_path))
    assert removed == 0

    # XML unchanged — all 3 items still present
    tree = ET.parse(site / "posts.xml")
    assert len(tree.getroot().find("channel").findall("item")) == 3


def test_feed_false_outside_frontmatter_ignored(tmp_path):
    """feed: false in body text (not YAML) should not trigger exclusion."""
    posts = tmp_path / "posts"
    posts.mkdir()
    site = tmp_path / "_site"
    site.mkdir()

    (posts / "qld.md").write_text(
        "---\ntitle: QLD\n---\nSome text\nfeed: false\nMore text\n"
    )
    (site / "posts.xml").write_text(SAMPLE_RSS)

    removed = clean_feed(str(tmp_path))
    assert removed == 0


def test_multiple_excluded(tmp_path):
    """Multiple posts with feed: false are all removed."""
    posts = tmp_path / "posts"
    posts.mkdir()
    site = tmp_path / "_site"
    site.mkdir()

    (posts / "qld.md").write_text("---\nfeed: false\n---\n")
    (posts / "China_update.md").write_text("---\nfeed: false\n---\n")
    (posts / "Longhaul.md").write_text("---\ntitle: Longhaul\n---\n")
    (site / "posts.xml").write_text(SAMPLE_RSS)

    removed = clean_feed(str(tmp_path))
    assert removed == 2

    tree = ET.parse(site / "posts.xml")
    items = tree.getroot().find("channel").findall("item")
    assert len(items) == 1
    assert items[0].find("link").text == "https://itkservices3.com/posts/Longhaul.html"
