"""Validate the public SEO files before deploying GitHub Pages."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
BASE_URL = "https://faramarzkowsari.github.io/computational-pathology-ai-lab"


class HeadInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = False
        self.canonical = False
        self.description = False
        self.robots = False
        self.json_ld_blocks: list[str] = []
        self._inside_json_ld = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self.title = True
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = True
        if tag == "meta" and values.get("name") == "description":
            self.description = True
        if tag == "meta" and values.get("name") == "robots":
            self.robots = True
        if tag == "script" and values.get("type") == "application/ld+json":
            self._inside_json_ld = True
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._inside_json_ld:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._inside_json_ld:
            self.json_ld_blocks.append("".join(self._buffer))
            self._inside_json_ld = False


def validate_html(path: Path, require_json_ld: bool = True) -> None:
    parser = HeadInspector()
    parser.feed(path.read_text(encoding="utf-8"))

    required = {
        "title": parser.title,
        "canonical": parser.canonical,
        "description": parser.description,
        "robots": parser.robots,
    }
    missing = [name for name, present in required.items() if not present]
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")

    if require_json_ld:
        if not parser.json_ld_blocks:
            raise ValueError(f"{path}: missing JSON-LD")
        for block in parser.json_ld_blocks:
            json.loads(block)


def validate_sitemap() -> None:
    path = WEBSITE / "sitemap.xml"
    tree = ET.parse(path)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [
        item.text
        for item in tree.findall(".//sm:loc", namespace)
        if item.text
    ]
    if not urls:
        raise ValueError("sitemap.xml contains no URLs")
    if any(not url.startswith(BASE_URL) for url in urls):
        raise ValueError("sitemap.xml contains a URL outside the project site")


def validate_robots() -> None:
    content = (WEBSITE / "robots.txt").read_text(encoding="utf-8")
    expected = f"Sitemap: {BASE_URL}/sitemap.xml"
    if "User-agent: *" not in content or "Allow: /" not in content:
        raise ValueError("robots.txt does not allow normal crawling")
    if expected not in content:
        raise ValueError("robots.txt does not reference the expected sitemap")


def main() -> None:
    validate_html(WEBSITE / "index.html")
    validate_html(WEBSITE / "book.html")
    validate_html(WEBSITE / "404.html", require_json_ld=False)
    validate_sitemap()
    validate_robots()
    print("SEO validation passed.")


if __name__ == "__main__":
    main()
