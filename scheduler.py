import time
import schedule
import subprocess
from datetime import datetime, timedelta

def job():
    subprocess.run(["scrapy", "crawl", "weather"], shell=True)

job()

schedule.every(3).minutes.do(job)
now = datetime.now()
delta = timedelta(minutes=10)
final_time = now + delta

while datetime.now() < final_time:
    schedule.run_pending()
    time.sleep(1)
    # print(datetime.datetime.now())