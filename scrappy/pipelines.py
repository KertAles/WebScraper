# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class scrappyPipeline:

    def __init__(self):
        self.conn = psycopg2.connect(
            host="postgres",
            port="5432",
            database="property",
            user="postgres",
            password="test")

        self.conn.autocommit = False

        self.cursor = self.conn.cursor()
        self.cursor.execute('SET client_encoding TO "UTF8"')

    def process_item(self, item, spider):
        #insert_command = f"INSERT INTO properties (address, img_url) VALUES" \
        #                 f" ('{item['address']}', '{item['img_url']}');"

        #self.cursor.execute(insert_command)

        self.cursor.execute(""" INSERT INTO properties (address, img_url) VALUES (%s,%s)""", (
            item["address"],
            item["img_url"]
        ))

        self.conn.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cursor.close()
        self.conn.close()
