# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector 


class BlackWidowPipeline:
    def __init__(self):
        self.create_connection()
    
    def create_connection(self):
        self.connection = mysql.connector.connect(
            host='rankidb.c39jpvgy5agc.us-east-2.rds.amazonaws.com',
            database='rankidb' ,
            user='admin',
            password='Phxntom10$!'
        )
        self.cursor = self.connection.cursor()
    
    def process_item(self,item,spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """INSERT INTO rankidb.queries 
                (query_name,cards,reddit_links,youtube_links,affiliate_links)  values (%s,%s,%s,%s,%s);    
            """, 
        (
            item['query_name'],
            item['cards'],
            item['reddit'],
            item['youtube'],
            item['google']
        ))
        self.cursor.execute("""UPDATE rankidb.queries SET query_name = trim(BOTH '"' FROM query_name)""")
        self.connection.commit()



# class ProductPipeline:
#     def __init__(self):
#         self.create_connection()
    
#     def create_connection(self):
#         self.connection = mysql.connector.connect(
#             host='rankidb.c39jpvgy5agc.us-east-2.rds.amazonaws.com',
#             database='rankidb' ,
#             user='admin',
#             password='Phxntom10$!'
#         )
#         self.cursor = self.connection.cursor()
    
#     def process_item(self,item,spider):
#         self.store_db(item)
#         return item

#     def store_db(self, item):
#         if item.__class__.__name__ == 'Product':
#             self.cursor.execute(
#                 """INSERT INTO rankidb.products 
#                     (
#                         product_title,product_description,product_rating,
#                         product_image,product_specs,link,all_reviews_link,
#                         buying_options_link,entity,buying_options,
#                         reviews,review_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
#                     );    
#                 """, 
#             (
#                 item['product_title'],
#                 item['product_description'],
#                 item['product_rating'],
#                 item['product_image'],
#                 item['product_specs'],
#                 item['link'],
#                 item['all_reviews_link'],
#                 item['buying_options_link'],
#                 item['entity'],
#                 item['buying_options'],
#                 item['reviews'],
#                 item['review_count']
#             ))
#             self.cursor.execute("""UPDATE rankidb.products SET product_title = trim(BOTH '"' FROM product_title)""")
#             self.connection.commit()


