import mysql.connector

class WeatherBotPipeline(object):

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="weather"
        )
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):

        self.curr.execute("""CREATE TABLE IF NOT EXISTS city(
            id int NOT NULL,
            name varchar(255),
            state varchar(255),
            PRIMARY KEY (id))""")

        self.curr.execute("""CREATE TABLE IF NOT EXISTS weather(
            city_id int NOT NULL,
            temperature int,
            humidity int,sensation int,
            windVelocity int,pressure int,
            date datetime,
            FOREIGN KEY (city_id) REFERENCES city(id))""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""INSERT IGNORE INTO city values(%s,%s,%s)""", (
            item["city_id"],
            item["city"],
            item["state"]))

        self.curr.execute("""INSERT INTO weather values(%s,%s,%s,%s,%s,%s,%s)""", (
            item["city_id"], item["temperature"], item["humidity"],
            item["sensation"], item["wind_velocity"], item["pressure"],
            item["date"]))

        self.conn.commit()