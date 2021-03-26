import time
import schedule
import subprocess
from datetime import datetime, timedelta

# Function to run the command scrapy crawl weather
def job():
    subprocess.run(["scrapy", "crawl", "weather"], shell=True)
# Running the spider as soon as the file is executed
job()

schedule.every(60).minutes.do(job)
now = datetime.now()
delta = timedelta(minutes=305)
final_time = now + delta

while datetime.now() < final_time:
    schedule.run_pending()
    time.sleep(1)