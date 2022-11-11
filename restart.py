import threading
import time
import schedule
import os



def os1():
    os.system("kill -9  $(ps aux | grep go-cqhttp | awk '{ print $2}')")
    os.system("kill -9  $(ps aux | grep python3.8 | awk '{ print $2}')")


def run_threaded(job_func):
     job_thread = threading.Thread(target=job_func)
     job_thread.start()


def os2():
    os.system("cd / ; cd /QQ-bot/go-cqhttp/ ; go-cqhttp")


def os3():
    os.system("cd / ; cd /QQ-bot/InceptionQQbot-master/ ; nb run")

# 每天重启
schedule.every().day.at("00:30").do(run_threaded, os1)
schedule.every().day.at("06:30").do(run_threaded, os2)
schedule.every().day.at("06:30").do(run_threaded, os3)
while True:
    schedule.run_pending()
    time.sleep(60)
