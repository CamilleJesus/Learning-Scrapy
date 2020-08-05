import scrapy

class GilenoFilhoSpider(scrapy.Spider):   #spider: unidade básica do Scrapy
    name = 'GilenoFilho'
    start_urls = ['http://www.gilenofilho.com.br']

    def parse(self, response):
        self.log("Hello, World!")
        self.log(response.body)

