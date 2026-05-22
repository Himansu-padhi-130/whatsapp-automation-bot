import schedule
import time

def job():
    print("Scheduler is running...")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)