import scrapy


class MusaSpider(scrapy.Spider):
    name = 'musa'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for each in response.xpath("//div[@class='product details product-item-details']"):
            yield {
                'name': each.xpath(".//h3/a/text()"),
                # 'price': each.xpath(".//")
            }
