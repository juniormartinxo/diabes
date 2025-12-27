# Crawler

Scrapy + Playwright project scaffold.

## Setup

```bash
pip install -r requirements.txt
playwright install
```

## Running

```bash
scrapy crawl site -a site=KEY_SITE
# or: CRAWLER_SITE=KEY_SITE scrapy crawl site
```

## Site config (.env)

```env
SITE_KEY_ALLOWED_DOMAINS=site.org
SITE_KEY_START_URLS=https://site.org/
SITE_KEY_USE_PLAYWRIGHT=true
SITE_KEY_WAIT_FOR_SELECTOR=body
```

Lists use comma separation for multiple domains/URLs.

## JS rendering

- Use `meta={"playwright": True}` on requests, or
- Use `BaseSpider.make_request(..., use_playwright=True)`.

Settings live in `crawler/settings.py`.
