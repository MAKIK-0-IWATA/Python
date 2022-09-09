import scrapy


class TestScrapingSpider(scrapy.Spider):
    name = 'test_scraping'
    allowed_domains = ['scraping-for-beginner.herokuapp.com/ranking']
    start_urls = ['https://scraping-for-beginner.herokuapp.com/ranking/']

    def parse(self, response):
        title = response.css('h2::text').getall()
        star = response.css("div.u_rankBox > span.evaluateNumber").getall()

        yield {
            'title': title,
            'star': star
        }
        pass
