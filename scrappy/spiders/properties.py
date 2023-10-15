import scrapy
from scrapy_selenium import SeleniumRequest

class PropertiesSpider(scrapy.Spider):
    name = "properties"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/hledani/prodej/komercni"]

    def start_requests(self):
        for url in self.start_urls :
            for i in range(25) :
                yield SeleniumRequest(url=url+f'?strana={i+1}', callback=self.parse, wait_time=10)



    def parse(self, response):
        for prop in response.css('div.property'):
            result = {
                'address': prop.css('span.locality::text').get(),
                'img_url': prop.css('.property img::attr(src)').extract_first()
            }

            yield result

