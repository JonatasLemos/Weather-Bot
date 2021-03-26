# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherBotItem(scrapy.Item):
    # define the fields for your item here like:
    city_id = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    temperature = scrapy.Field()
    humidity = scrapy.Field()
    sensation = scrapy.Field()
    wind_velocity = scrapy.Field()
    pressure = scrapy.Field()
    date = scrapy.Field()
