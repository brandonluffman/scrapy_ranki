# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RankiQuery(scrapy.Item):
    query_name = scrapy.Field()
    entities = scrapy.Field()
    card_links = scrapy.Field()
    card_descriptions = scrapy.Field()
    reddit = scrapy.Field()
    youtube = scrapy.Field()
    google = scrapy.Field()
