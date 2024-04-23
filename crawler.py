import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import CloseSpider

class BeethovenCrawler(scrapy.Spider):
    name = 'beethoven_crawler'
    start_urls = ['https://en.wikipedia.org/wiki/Ludwig_van_Beethoven']
    allowed_domains = ['wikipedia.org']
    custom_settings = {
        'DEPTH_LIMIT': 2,  # Adjust max depth as needed
        'CONCURRENT_REQUESTS': 16,  # Adjust concurrency as needed
        'AUTOTHROTTLE_ENABLED': True,
        'FILES_STORE_ENC': 'utf-8',  # Store HTML in UTF-8
    }

    def parse(self, response):
        # Extract content using BeautifulSoup or other selectors
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.body, 'html.parser')

        content = soup.find('div', id='mw-content-text').get_text(strip=True)

        # Save to file (optional, adjust file naming)
        filename = f'beethoven_{response.url.split("/")[-1]}.html'
        self.crawler.store.persist_item({'content': content}, filename)

        # Follow outgoing links within allowed domains (optional)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('/') and href not in self.crawler.spidercls.seen_urls:
                self.crawler.spidercls.seen_urls.add(href)
                yield response.follow(href, self.parse)

        # Limit downloaded pages (optional)
        if len(self.crawler.engine.scraper.crawled) >= self.crawler.settings['DEPTH_LIMIT']:
            raise CloseSpider(reason='Max pages crawled')

class BeethovenContentPipeline(FilesPipeline):
    def file_url(self, item, info):
        return item['filename']

    def get_media_requests(self, item, info):
        yield scrapy.Request(url='about:blank')

    def item_completed(self, results, item, info):
        return item
