import scrapy
import time

limit = False
infty = 1000000

class Player(scrapy.Item):
    name = scrapy.Field()
    team = scrapy.Field()
    passport = scrapy.Field()
    birth_date = scrapy.Field()
    height = scrapy.Field()
    position = scrapy.Field()

class NewSpider(scrapy.Spider):
    name = 'players'

    def start_requests(self):
        try:
            with open("links.csv") as f:
                start_urls = [url.strip() for url in f.readlines()][1:]
        except:
            start_urls = []
        counter = infty
        if limit:
            counter = 100
        Start = time.time()
        for url in start_urls:
            if counter > 0:
                yield scrapy.Request(url=url, callback=self.parse)
                counter = counter - 1
        End =time.time()
        Total = End-Start
        print('Crawling time:', Total)
    def parse(self, response):
        p = Player()
        p['name'] = response.css('title::text').get()
        p['team'] = response.css('div.col-xl-6.col-lg-6.col-md-6.col-sm-12.mycol').css('li::text').get().replace('-', '').replace('  ', '')
        data = response.css('div.col-6.numer').css('span::text').getall()
        p['passport'] = data[0]
        p['birth_date'] = data[1]
        p['height'] = data[2]
        p['position'] = data[3]

        yield p