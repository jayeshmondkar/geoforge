import requests
from bs4 import BeautifulSoup


def safe_fetch(url):
    try:
        response = requests.get(url, timeout=10)

        # Always use raw bytes + safe decode
        content = response.content

        try:
            return content.decode("utf-8")
        except:
            return content.decode("latin-1", errors="ignore")

    except:
        return ""


def crawl_site(url, max_pages=10, manual_urls=None):
    pages = []

    # ---------------------------
    # MANUAL MODE
    # ---------------------------
    if manual_urls:
        if len(manual_urls) > max_pages:
            return {
                "error": "LIMIT_EXCEEDED",
                "message": "Free plan allows max 10 pages. Upgrade required."
            }

        for link in manual_urls:
            html = safe_fetch(link)
            if html:
                pages.append(html)

        return pages

    # ---------------------------
    # AUTO MODE
    # ---------------------------
    visited = set()

    html = safe_fetch(url)
    if not html:
        return pages

    soup = BeautifulSoup(html, "html.parser")

    links = [a.get("href") for a in soup.find_all("a", href=True)]

    for link in links:
        if len(pages) >= max_pages:
            break

        if link.startswith("http") and link not in visited:
            page_html = safe_fetch(link)

            if page_html:
                pages.append(page_html)
                visited.add(link)

    return pages