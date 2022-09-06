import scrapy


class TestScrapingSpider(scrapy.Spider):
    name = 'test_scraping'
    allowed_domains = ['scraping-for-beginner.herokuapp.com/ranking']
    start_urls = ['https://scraping-for-beginner.herokuapp.com/ranking/']

    def parse(self, response):
        pass
