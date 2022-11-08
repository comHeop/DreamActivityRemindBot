# -*- coding: UTF-8 -*-
import schedule
import os


def stra():
    os.system("kill -9  $(ps aux | grep go-cqhttp | awk '{ print $2}')")
    os.system("kill -9  $(ps aux | grep python3.8 | awk '{ print $2}')")
    os.system('cd InceptionQQbot-master/ ; nb run')
    os.system('cd cd go-cqhttp/ ; go-cqhttp')


schedule.every().day.at("04:00").do(stra)  # 每天4点重启

while True:
    schedule.run_pending()  # 运行所有可运行的任务
