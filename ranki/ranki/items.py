# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RankiQuery(scrapy.Item):
    query_name = scrapy.Field()
    cards = scrapy.Field()
    reddit = scrapy.Field()
    youtube = scrapy.Field()
    google = scrapy.Field()


# class Product(scrapy.Item):
#     product_title = scrapy.Field()
#     product_description = scrapy.Field()
#     product_rating = scrapy.Field()
#     product_image = scrapy.Field()
#     product_specs = scrapy.Field()
#     link = scrapy.Field()
#     all_reviews_link = scrapy.Field()
#     buying_options_link = scrapy.Field()
#     entity = scrapy.Field()
#     buying_options = scrapy.Field()
#     reviews = scrapy.Field()
#     review_count = scrapy.Field()