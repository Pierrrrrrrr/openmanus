"""Angel that performs basic web scraping."""
from __future__ import annotations

import requests
from bs4 import BeautifulSoup

from . import Angel, Task


class ScraperAngel(Angel):
    name = "scraper_angel"

    def run(self, task: Task) -> tuple[str, list[Task]]:
        url = str(task.data or "")
        if not url:
            return "No URL provided", []
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string if soup.title else "no title"
            return f"Scraped title: {title}", []
        except Exception as exc:  # pragma: no cover - external network
            return f"Scraping failed: {exc}", []
