import scrapy


class PaginationSpider(scrapy.Spider):
    name = 'pagination'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75.html']

    def parse(self, response):
        for each in response.xpath("//div[@class='r_b_c']/div[@class='p_box_wrapper']/div"):
            taka = each.xpath(".//div[@class= 'p_box_price cf']/text()").get()
            if taka == None:
                price = each.xpath(".//div[@class= 'p_box_price cf']/span[@class='productSpecialPrice fl']/text()").get()
            else:
                price = taka
            yield {
                "name": each.xpath(".//a[@class='p_box_title']/text()").get(),
                "link": response.urljoin(each.xpath(".//a[@class='p_box_title']/@href").get()),
                "number of times bought": each.xpath(".//div[@class = 'p_box_star']/a/text()").get(),
                'price': price
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)