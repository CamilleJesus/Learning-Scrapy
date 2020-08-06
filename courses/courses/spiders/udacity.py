import scrapy
import base64


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    #allowed_domains = ['https://www.udacity.com/courses/all']
    start_urls = ['https://www.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/main/div[2]/ul/li')
        
        for div in divs:
            title = div.xpath(".//h2/text()").extract_first()
            skills = div.xpath(".//section/p/text()").extract_first()
            details = div.xpath(".//div/p/text()").extract_first()
            school = div.xpath(".//h3/text()").extract_first()
            image = div.xpath('.//div[@class="card__image"]/@style').extract_first()

            yield {
                'title': title,
                'skills': skills,
                'details': details,
                'school': school,
                'image': image,
            }
