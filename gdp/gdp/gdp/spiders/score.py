import scrapy


class ScoreSpider(scrapy.Spider):
    name = 'score'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        target = response.xpath("//td/a")
        data = 0
        for each in target:
            data = data + 1
            name = each.xpath(".//text()").get()
            link = each.xpath(".//@href").get()
            
            yield response.follow(link,callback=self.country_parse,meta={'country_name':name,'int':data})

    def country_parse(self, response):
        row = response.xpath("(//table[@class='jsx-1487038798 table table-striped tp-table-body'])[3]/tbody/tr")
        data = response.request.meta['int']
        name = response.request.meta['country_name']

        for each in row:
            year = each.xpath(".//td[1]/text()").get()
            population = each.xpath(".//td[2]/text()").get()

            yield {
                'int': data,
                'name':name,
                'Future_year':year,
                'Predicted_population': population
            }