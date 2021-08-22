import scrapy


class BidSpider(scrapy.Spider):
    name = 'bid'
    allowed_domains = ['www.bidnetdirect.com']
    start_urls = ['https://www.bidnetdirect.com/solicitations/open-bids/']

    def parse(self, response):
        for each in response.xpath("//table[@id='solicitationsList']/tbody/tr"):
            yield {
                'name': each.xpath(".//td[1]/a/text()").get(),
                'Location': each.xpath(".//td[2]/text()").get(),
                'Publishing Date': each.xpath(".//td[3]/text()").get(),
                'Closing Date': each.xpath(".//td[4]/text()").get(),
            }
        next_page = response.xpath("//a[@class='next mets-pagination-page-icon']/@href").get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url = next_page, callback=self.parse)