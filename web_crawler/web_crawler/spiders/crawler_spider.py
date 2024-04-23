import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Ludwig_van_Beethoven']

    def parse(self, response):
        # Extracting content from the webpage
        title = response.css('h1.firstHeading::text').get()
        content = response.css('div#mw-content-text p::text').getall()

        yield {
            'title': title,
            'content': ' '.join(content)
        }