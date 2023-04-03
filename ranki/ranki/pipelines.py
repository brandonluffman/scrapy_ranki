# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import mysql.connector 

class BlackWidowPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='rankidb.c39jpvgy5agc.us-east-2.rds.amazonaws.com',
            database='rankidb' ,
            user='admin',
            password='Phxntom10$!'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if 'query_name' in item:
            query = """INSERT INTO rankidb.queries 
                        (query_name,cards,reddit_links,youtube_links,affiliate_links) values (%s,%s,%s,%s,%s);    
                    """
            values = (
                item['query_name'],
                item['cards'],
                item['reddit'],
                item['youtube'],
                item['google'])
            self.cursor.execute(query, values)
            self.cursor.execute("""UPDATE rankidb.queries SET query_name = trim(BOTH '"' FROM query_name)""")
            self.conn.commit()
        elif 'product_title' in item:
            query ="""INSERT INTO rankidb.products 
                        (
                            product_title,product_description,product_rating,
                            product_image,product_specs,link,all_reviews_link,
                            buying_options_link,entity,buying_options,
                            reviews,review_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                        );    
                    """
            values = (
                        item['product_title'],
                        item['product_description'],
                        item['product_rating'],
                        item['product_image'],
                        item['product_specs'],
                        item['link'],
                        item['all_reviews_link'],
                        item['buying_options_link'],
                        item['entity'],
                        item['buying_options'],
                        item['reviews'],
                        item['review_count']
                    )
            self.cursor.execute(query, values)
            self.cursor.execute("""UPDATE rankidb.products SET product_title = trim(BOTH '"' FROM product_title)""")
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()