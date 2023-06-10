# Webscraping-PolishBasketballLeague-UW2023
Web scraping project on Polish Basketball League players, conducted by Hande Demirci, Antoni Piotrowski, and Aleksandra Wiśniewska.


## Scrapy


The first spider crawls through the page to extract required links:

Program defines a Scrapy spider named "suzuki" by subclassing the 'scrapy.Spider' class.
Spider starts crawling from the provided URL.
In the parse method, the spider receives the response from the initial URL.
It extracts the links to individual player profiles from the HTML response using CSS selectors.
The number of links to extract is determined by the counter variable, which is set to a large value (infty) or a specific limit (100) depending on the value of the limit flag.
The extracted links are appended to a list called links.
The program creates a pandas DataFrame using the links list, where each row represents a link.
The DataFrame is then saved to a CSV file named "links.csv" using the to_csv method.
Finally, the program prints each item (link) in the links list.

Second one collects needed data from every link of input csv file:

It defines a Scrapy item class called Player to store players information.
It defines a Scrapy spider class called NewSpider that inherits from scrapy.Spider.
The spider class defines the start_requests method, which reads the URLs from a file called "links.csv" and initiates requests to each URL.
If the limit flag is set to False, the spider processes all URLs. Otherwise, if limit is set to True, the spider only processes a maximum of 100 URLs.
The spider measures the start time before making the requests.
For each URL, the spider sends a request and assigns the callback method parse to handle the response.
The parse method is responsible for extracting player information from the response using CSS selectors and populating the Player item.
The extracted player data is yielded as output, which is collected by Scrapy.
After processing all URLs, the spider measures the end time and calculates the crawling time.
Finally, the crawling time is printed to the console.
