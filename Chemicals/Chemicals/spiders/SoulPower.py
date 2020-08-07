import scrapy


class SoulpowerSpider(scrapy.Spider):
    name = 'SoulPower'
    #allowed_domains = ['soulpowerbrasil.com.br/produtos']
    start_urls = ['http://soulpowerbrasil.com.br/produto/no-bubble-315ml']

    def parse(self, response):
        title = response.xpath(".//h2[@class = 'ff-oswald fw-bold fc-preto col-xs-12 no-padding']/text()").extract_first()
        kind = response.xpath(".//h3[@class = 'ff-oswald fw-light fc-rosa1 col-xs-12 no-padding']/text()").extract_first()
        ph = response.xpath(".//h3[@class = 'ff-oswald fw-light fc-roxo1 col-xs-12 no-padding']/text()").extract_first()
        description = response.xpath(".//article[@class = 'descricao ff-oswald fw-light col-xs-12 no-padding']/text()[1]").extract_first()
        #seals = response.xpath(".//section[1]/div[2]/div/div/img").extract()
        image = response.xpath(".//img[@class='img-responsive transition-padrao no-padding']/@src").extract()
        
        yield {
            'title': title,
            'kind': kind,
            'ph': ph,
            'description': description,
            #'seals': seals,
            'image': image,
        }

        for curl in response.xpath("//a[contains(@href, 'http://soulpowerbrasil.com.br/produtos?categoria=')]"):
            print(curl.xpath(".//li/span/text()").extract_first())
        
