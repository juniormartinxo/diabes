import scrapy

from crawler.services.playwright import build_playwright_meta


class BaseSpider(scrapy.Spider):
    def make_request(
        self,
        url: str,
        callback,
        *,
        use_playwright: bool = False,
        wait_for_selector: str | None = None,
        page_methods=None,
        **kwargs,
    ) -> scrapy.Request:
        meta = kwargs.pop("meta", {}) or {}

        if use_playwright:
            meta.update(
                build_playwright_meta(
                    wait_for_selector=wait_for_selector,
                    page_methods=page_methods,
                )
            )

        return scrapy.Request(url, callback=callback, meta=meta, **kwargs)

    def parse(self, response):
        raise NotImplementedError("Spiders must implement parse")
