# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import mysql.connector 


# class BlackWidowPipeline:
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
#         self.cursor.execute(
#             """INSERT INTO rankidb.queries 
#                 (query_name,entities,cards,reddit_links,youtube_links,affiliate_links)  values (%s,%s,%s,%s,%s)""", 
#         (
#             item["query_name"],
#             item["cards"],
#             item['reddit'],
#             item['youtube'],
#             item['google']
#         ))
#         self.connection.commit()



