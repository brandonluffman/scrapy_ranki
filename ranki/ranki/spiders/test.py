import scrapy
from newspaper import Article
from newspaper import Config


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["http://google.com/"]

    

    def parse(self, response): 
        for serp_link in serp_link_list:
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            config = Config()
            config.browser_user_agent = user_agent

            try:
                article = Article(serp_link, config=config)
                article.download()
                article.parse()
            except:
                pass
