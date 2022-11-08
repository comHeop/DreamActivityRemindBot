import schedule
import os

# 每天4点重启
schedule.every().day.at("04:00").do(os.system("kill -9  $(ps aux | grep go-cqhttp | awk '{ print $2}')"))
schedule.every().day.at("04:00").do(os.system("kill -9  $(ps aux | grep python3.8 | awk '{ print $2}')"))
schedule.every().day.at("04:01").do(os.system("cd InceptionQQbot-master/ ; nb run"))
schedule.every().day.at("04:02").do(os.system("cd go-cqhttp/ ; go-cqhttp"))

while True:
    schedule.run_pending()  # 运行所有可运行的任务
