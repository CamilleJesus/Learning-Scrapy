import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    #allowed_domains = ['https://pt.coursera.org/']
    start_urls = ['https://pt.coursera.org//']

    def parse(self, response):
        self.log("Hello, Scrapy Project!")
        self.log(response)
