from itemadapter import ItemAdapter

from crawler.utils.parsing import normalize_whitespace
from crawler.utils.urls import normalize_url


class CleanPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if "title" in adapter:
            adapter["title"] = normalize_whitespace(adapter.get("title"))

        if "url" in adapter:
            adapter["url"] = normalize_url(adapter.get("url", ""))

        if "content" in adapter:
            adapter["content"] = normalize_whitespace(adapter.get("content"))

        return item
