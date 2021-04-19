import scrapy
import json
from ..items import WeatherBotItem

class AllSpider(scrapy.Spider):

    name = "weather"
    allowed_domains = ["climatempo.com.br"]
    start_urls = ["https://www.climatempo.com.br/json/myclimatempo/user/weatherNow?idlocale=3477"]

    def parse(self, response):

        result = json.loads(response.body)

        items = WeatherBotItem()

        locale = result[0]["data"][0]["locale"]
        weather = result[0]["data"][0]["weather"][0]

        items["city_id"] = locale["id"]
        items["city"] = locale["name"]
        items["state"] = locale["uf"]
        items["temperature"] = weather["temperature"]
        items["humidity"] = weather["humidity"]
        items["sensation"] = weather["sensation"]
        items["wind_velocity"] = weather["windVelocity"]
        items["pressure"] = weather["pressure"]
        items["date"] = weather["date"]

        yield items

        ids = [8909, 7644, 5799, 3740, 3569, 4625, 5975]
        for city_id in ids:
            yield scrapy.Request(
                url=f"https://www.climatempo.com.br/json/myclimatempo/user/weatherNow?idlocale={city_id}",
                callback=self.parse)
        


