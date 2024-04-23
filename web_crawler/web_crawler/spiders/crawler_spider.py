import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Ludwig_van_Beethoven']
    visited_urls = set()

    def parse(self, response):
        # Extracting content from the webpage
        title = response.css('h1.firstHeading::text').get()
        content = response.css('div#mw-content-text p::text').getall()

        yield {
            'title': title,
            'content': ' '.join(content)
        }

        # Add the current URL to the set of visited URLs
        self.visited_urls.add(response.url)

        # Extract links from the current page and follow them if not visited and within depth limit
        links = response.css('a::attr(href)').getall()
        for link in links:
            if link and link.startswith('/') and link not in self.visited_urls:
                yield response.follow(link, callback=self.parse)
            elif link and link.startswith('https://en.wikipedia.org') and link not in self.visited_urls:
                yield response.follow(link, callback=self.parse)