from scrapy.linkextractors import LinkExtractor

class YahoofinanceNewsLinkExtractor(LinkExtractor):
  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)