import scrapy


class NoPooSpider(scrapy.Spider):
    name = 'no_poo'
    #allowed_domains = ['www.dermabox.com.br/no-poo']
    start_urls = ['http://www.dermabox.com.br/no-poo']

    def parse(self, response):
        divs = response.xpath('//*[@id="listagemProdutos"]/ul/li')
        
        for div in divs:
            title = div.xpath(".//a/text()").extract_first()
            href = div.xpath(".//a/@href").extract_first()
            price = div.xpath('.//strong[@class="preco-promocional cor-principal titulo"]/text()').extract_first()
            price = price.split("R$ ")[1].split("\n")[0]
            
            yield {
                'title': title,
                'href': href,
                'price': price,
            }
