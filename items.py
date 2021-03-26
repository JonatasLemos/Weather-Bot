import scrapy

class WeatherBotItem(scrapy.Item):
    city_id = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    temperature = scrapy.Field()
    humidity = scrapy.Field()
    sensation = scrapy.Field()
    wind_velocity = scrapy.Field()
    pressure = scrapy.Field()
    date = scrapy.Field()
