#!/usr/bin/env python3
"""Fetch latest Weekly Sync episodes from RSS and update podcast pages."""

import urllib.request
import xml.etree.ElementTree as ET
import re
import os

RSS_URL = "https://feeds.megaphone.fm/POLTD1514843688"
SPOTIFY_FALLBACK = "https://open.spotify.com/show/674Fd3udoDREXmBq44dHWY"
NUM_EPISODES = 5

# Paths relative to repo root
REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
HE_PODCAST = os.path.join(REPO_ROOT, "he", "podcast", "index.html")
HE_HOME = os.path.join(REPO_ROOT, "he", "index.html")


def fetch_episodes():
    """Fetch latest episodes from RSS feed."""
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "tortsuk-bot/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)
    episodes = []
    for item in root.iter("item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip() or SPOTIFY_FALLBACK
        if title:
            episodes.append({"title": title, "link": link})
        if len(episodes) >= NUM_EPISODES:
            break

    return episodes


def build_list_html(episodes):
    """Build <ul> inner HTML from episodes."""
    lines = []
    for ep in episodes:
        safe_title = ep["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe_link = ep["link"].replace("&", "&amp;")
        lines.append(
            f'        <li>\n'
            f'          <a href="{safe_link}" target="_blank">{safe_title}</a>\n'
            f'        </li>'
        )
    return "\n".join(lines)


def update_html_file(filepath, episodes):
    """Replace episode list in an HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    list_html = build_list_html(episodes)

    # Match the <ul> with id or class episode-list and replace its contents
    pattern = r'(<ul[^>]*class="episode-list"[^>]*>)\s*.*?\s*(</ul>)'
    replacement = rf'\1\n{list_html}\n      \2'
    new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")


def main():
    print("Fetching RSS feed...")
    episodes = fetch_episodes()
    print(f"Found {len(episodes)} episodes")

    for ep in episodes:
        print(f"  - {ep['title']}")

    update_html_file(HE_PODCAST, episodes)
    update_html_file(HE_HOME, episodes[:2])


if __name__ == "__main__":
    main()
