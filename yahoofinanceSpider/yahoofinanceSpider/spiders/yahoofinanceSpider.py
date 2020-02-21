import scrapy
from scrapy.spiders import CrawlSpider, Rule
from yahoofinanceSpider.items import *
from yahoofinanceSpider.linkExtractors import YahoofinanceNewsLinkExtractor
from datetime import datetime, date

class YahoofinanceSpider(CrawlSpider):
    name = "Yahoofinance"
    start_urls = []
    # start_urls.append("https://finance.yahoo.com")
    start_urls.append("https://ca.finance.yahoo.com")
    allowed_domains = ["finance.yahoo.com"]
    rules = (
        Rule(YahoofinanceNewsLinkExtractor(allow=('news/*', )), callback='parseNews'),
    )

    def parseNews(self, response):
        news = NewsItem()
        news["title"] = response.xpath(".//header/h1/text()").get()
        rowDateString = response.xpath(".//time/@datetime").get()
        news["date"] = datetime.strptime(rowDateString, '%Y-%m-%dT%H:%M:%S.%fZ')
        yield news
