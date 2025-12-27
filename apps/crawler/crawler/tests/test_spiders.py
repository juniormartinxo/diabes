from scrapy_playwright.page import PageMethod

from crawler.spiders.base import BaseSpider


class DummySpider(BaseSpider):
    name = "dummy"


def test_make_request_playwright_meta():
    spider = DummySpider()
    request = spider.make_request(
        "https://example.com",
        callback=spider.parse,
        use_playwright=True,
        wait_for_selector="body",
    )

    assert request.meta["playwright"] is True
    assert "playwright_page_methods" in request.meta
    methods = request.meta["playwright_page_methods"]
    assert methods
    assert isinstance(methods[0], PageMethod)
