import scrapy
import time

start  = time.time()

class PageSpider(scrapy.Spider):
    name = 'page'
    allowed_domains = ['www.bidnetdirect.com']
    start_urls = ['https://www.bidnetdirect.com/solicitations/open-bids?selectedContent=AGGREGATE']

    def parse(self, response):

        for each in response.xpath("//table[@id='solicitationsList']/tbody/tr"):
            yield {
                'name': each.xpath(".//td[1]/a/text()").get(),
                'state': each.xpath("normalize-space(.//td[2]/text())").get(),
                'published': each.xpath("normalize-space(.//td[3]/text())").get(),
                'closing': each.xpath("normalize-space(.//td[4]/text())").get(),
            }

        next_page = response.xpath("//a[@class= 'next mets-pagination-page-icon']/@href").get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url = next_page, callback = self.parse)
        else:
            end = time.time()
            print(end-start)
            yield {'time':end-start}

        # yield {
        #     'n':print(response.xpath("//table[@id='solicitationsList']/tbody/tr")),
        #     'f':print("/t This is without get method"),
        # print(response.xpath("//table[@id='solicitationsList']/tbody/tr").getall())
        # print("/t This is with get method")
        # print(response.xpath("//table[@id='solicitationsList']/tbody/tr").get())