import scrapy
import pandas as pd

limit = True
infty = 1000000

class NewSpider(scrapy.Spider):
    name = 'suzuki'
    start_urls = ['https://1lm.pzkosz.pl/zawodnicy.html']

    def parse(self, response):
        links = []
        counter = infty
        if limit:
            counter = 100
        for element in response.css('div.playersonlist.col-xl-3.col-lg-3.col-md-4.col-sm-6'):
            if counter > 0:
                link = 'https://1lm.pzkosz.pl' + element.css('a::attr(href)').get()
                links.append(link)
                counter = counter - 1

        # Create a DataFrame with the links
        df = pd.DataFrame({'link': links})

        # Save the DataFrame to a CSV file
        df.to_csv('links.csv', index=False)

        for item in links:
            print(item)
            # yield item