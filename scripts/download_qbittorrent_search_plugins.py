#!/usr/bin/env python3
"""Scrape qbittorrent unofficial search plugins wiki for .py links.

Usage:
  python download_qbittorrent_search_plugins.py | xargs -n1 wget -P plugins/
  # then in qBittorrent: View -> Search Engine -> Search plugins -> Install a new one
"""

import argparse
import re
import sys
import requests
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(description="List .py search plugin URLs from qbittorrent wiki")
    parser.add_argument(
        "--url",
        default="https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins",
        help="Wiki page to scrape"
    )
    args = parser.parse_args()

    try:
        resp = requests.get(args.url, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"error fetching: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(resp.content, "html.parser")
    links = soup.find_all(href=re.compile(r"\.py$"))

    for a in links:
        href = a.get("href", "")
        if href:
            # GitHub wiki links are often relative; make absolute if needed
            if href.startswith("/"):
                href = "https://github.com" + href
            print(href)


if __name__ == "__main__":
    main()

