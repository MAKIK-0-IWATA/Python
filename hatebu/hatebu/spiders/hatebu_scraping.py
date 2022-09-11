import scrapy


class HatebuScrapingSpider(scrapy.Spider):
    name = 'hatebu-scraping'
    allowed_domains = [
        'https://b.hatena.ne.jp/q/%E3%83%9A%E3%83%83%E3%83%88?target=text']
    start_urls = [
        'http://https://b.hatena.ne.jp/q/%E3%83%9A%E3%83%83%E3%83%88?target=text/']

    def parse(self, response):
        title = response.xpath(
            '//*[@id="container"]/div[2]/div[2]/ul/li/div/h3/a/text()').getall()
        url = response.xpath(
            '//*[@id="container"]/div[2]/div[2]/ul/li/div/h3/a/@href').getall()
        user = response.xpath(
            '//*[@id="container"]/div[2]/div[2]/ul/li/div[1]/ul/li[1]/span/a/text()').getall()

        yield {
            'title': title,
            'url': url,
            'user': user
        }
