import nonebot
from nonebot import require
import time

from nonebot.adapters.onebot.v11 import PRIVATE, GROUP, PRIVATE_FRIEND
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

from cj.到梦空间抢活动.config import updateConfiguration
from cj.到梦空间活动提醒.到梦空间活动提醒 import activeQuery

scheduler = require('nonebot_plugin_apscheduler').scheduler

qun = 760861972


# 设置在几点启动脚本
@scheduler.scheduled_job('cron', hour=7, minute=25)
@scheduler.scheduled_job('cron', hour=8, minute=25)
@scheduler.scheduled_job('cron', hour=9, minute=25)
@scheduler.scheduled_job('cron', hour=10, minute=25)
@scheduler.scheduled_job('cron', hour=11, minute=25)
@scheduler.scheduled_job('cron', hour=12, minute=25)
@scheduler.scheduled_job('cron', hour=13, minute=25)
@scheduler.scheduled_job('cron', hour=14, minute=25)
@scheduler.scheduled_job('cron', hour=15, minute=25)
@scheduler.scheduled_job('cron', hour=16, minute=25)
@scheduler.scheduled_job('cron', hour=17, minute=25)
@scheduler.scheduled_job('cron', hour=18, minute=25)
@scheduler.scheduled_job('cron', hour=19, minute=25)
@scheduler.scheduled_job('cron', hour=20, minute=25)
@scheduler.scheduled_job('cron', hour=21, minute=25)
@scheduler.scheduled_job('cron', hour=22, minute=25)
@scheduler.scheduled_job('cron', hour=23, minute=25)
@scheduler.scheduled_job('cron', hour=0, minute=25)
@scheduler.scheduled_job('cron', hour=7, minute=17)
@scheduler.scheduled_job('cron', hour=8, minute=17)
@scheduler.scheduled_job('cron', hour=9, minute=17)
@scheduler.scheduled_job('cron', hour=10, minute=17)
@scheduler.scheduled_job('cron', hour=11, minute=17)
@scheduler.scheduled_job('cron', hour=12, minute=17)
@scheduler.scheduled_job('cron', hour=13, minute=17)
@scheduler.scheduled_job('cron', hour=14, minute=17)
@scheduler.scheduled_job('cron', hour=15, minute=17)
@scheduler.scheduled_job('cron', hour=16, minute=17)
@scheduler.scheduled_job('cron', hour=17, minute=17)
@scheduler.scheduled_job('cron', hour=18, minute=17)
@scheduler.scheduled_job('cron', hour=19, minute=17)
@scheduler.scheduled_job('cron', hour=20, minute=17)
@scheduler.scheduled_job('cron', hour=21, minute=17)
@scheduler.scheduled_job('cron', hour=22, minute=17)
@scheduler.scheduled_job('cron', hour=23, minute=17)
@scheduler.scheduled_job('cron', hour=0, minute=17)
@scheduler.scheduled_job('cron', hour=7, minute=10)
@scheduler.scheduled_job('cron', hour=8, minute=10)
@scheduler.scheduled_job('cron', hour=9, minute=10)
@scheduler.scheduled_job('cron', hour=10, minute=10)
@scheduler.scheduled_job('cron', hour=11, minute=10)
@scheduler.scheduled_job('cron', hour=12, minute=10)
@scheduler.scheduled_job('cron', hour=13, minute=10)
@scheduler.scheduled_job('cron', hour=14, minute=10)
@scheduler.scheduled_job('cron', hour=15, minute=10)
@scheduler.scheduled_job('cron', hour=16, minute=10)
@scheduler.scheduled_job('cron', hour=17, minute=10)
@scheduler.scheduled_job('cron', hour=18, minute=10)
@scheduler.scheduled_job('cron', hour=19, minute=10)
@scheduler.scheduled_job('cron', hour=20, minute=10)
@scheduler.scheduled_job('cron', hour=21, minute=10)
@scheduler.scheduled_job('cron', hour=22, minute=10)
@scheduler.scheduled_job('cron', hour=23, minute=10)
@scheduler.scheduled_job('cron', hour=0, minute=10)
@scheduler.scheduled_job('cron', hour=7, minute=3)
@scheduler.scheduled_job('cron', hour=8, minute=3)
@scheduler.scheduled_job('cron', hour=9, minute=3)
@scheduler.scheduled_job('cron', hour=10, minute=3)
@scheduler.scheduled_job('cron', hour=11, minute=3)
@scheduler.scheduled_job('cron', hour=12, minute=3)
@scheduler.scheduled_job('cron', hour=13, minute=3)
@scheduler.scheduled_job('cron', hour=14, minute=3)
@scheduler.scheduled_job('cron', hour=15, minute=3)
@scheduler.scheduled_job('cron', hour=16, minute=3)
@scheduler.scheduled_job('cron', hour=17, minute=3)
@scheduler.scheduled_job('cron', hour=18, minute=3)
@scheduler.scheduled_job('cron', hour=19, minute=3)
@scheduler.scheduled_job('cron', hour=20, minute=3)
@scheduler.scheduled_job('cron', hour=21, minute=3)
@scheduler.scheduled_job('cron', hour=22, minute=3)
@scheduler.scheduled_job('cron', hour=23, minute=3)
@scheduler.scheduled_job('cron', hour=0, minute=3)
@scheduler.scheduled_job('cron', hour=7, minute=32)
@scheduler.scheduled_job('cron', hour=8, minute=32)
@scheduler.scheduled_job('cron', hour=9, minute=32)
@scheduler.scheduled_job('cron', hour=10, minute=32)
@scheduler.scheduled_job('cron', hour=11, minute=32)
@scheduler.scheduled_job('cron', hour=12, minute=32)
@scheduler.scheduled_job('cron', hour=13, minute=32)
@scheduler.scheduled_job('cron', hour=14, minute=32)
@scheduler.scheduled_job('cron', hour=15, minute=32)
@scheduler.scheduled_job('cron', hour=16, minute=32)
@scheduler.scheduled_job('cron', hour=17, minute=32)
@scheduler.scheduled_job('cron', hour=18, minute=32)
@scheduler.scheduled_job('cron', hour=19, minute=32)
@scheduler.scheduled_job('cron', hour=20, minute=32)
@scheduler.scheduled_job('cron', hour=21, minute=32)
@scheduler.scheduled_job('cron', hour=22, minute=32)
@scheduler.scheduled_job('cron', hour=23, minute=32)
@scheduler.scheduled_job('cron', hour=0, minute=32)
@scheduler.scheduled_job('cron', hour=7, minute=47)
@scheduler.scheduled_job('cron', hour=8, minute=47)
@scheduler.scheduled_job('cron', hour=9, minute=47)
@scheduler.scheduled_job('cron', hour=10, minute=47)
@scheduler.scheduled_job('cron', hour=11, minute=47)
@scheduler.scheduled_job('cron', hour=12, minute=47)
@scheduler.scheduled_job('cron', hour=13, minute=47)
@scheduler.scheduled_job('cron', hour=14, minute=47)
@scheduler.scheduled_job('cron', hour=15, minute=47)
@scheduler.scheduled_job('cron', hour=16, minute=47)
@scheduler.scheduled_job('cron', hour=17, minute=47)
@scheduler.scheduled_job('cron', hour=18, minute=47)
@scheduler.scheduled_job('cron', hour=19, minute=47)
@scheduler.scheduled_job('cron', hour=20, minute=47)
@scheduler.scheduled_job('cron', hour=21, minute=47)
@scheduler.scheduled_job('cron', hour=22, minute=47)
@scheduler.scheduled_job('cron', hour=23, minute=47)
@scheduler.scheduled_job('cron', hour=0, minute=47)
@scheduler.scheduled_job('cron', hour=7, minute=40)
@scheduler.scheduled_job('cron', hour=8, minute=40)
@scheduler.scheduled_job('cron', hour=9, minute=40)
@scheduler.scheduled_job('cron', hour=10, minute=40)
@scheduler.scheduled_job('cron', hour=11, minute=40)
@scheduler.scheduled_job('cron', hour=12, minute=40)
@scheduler.scheduled_job('cron', hour=13, minute=40)
@scheduler.scheduled_job('cron', hour=14, minute=40)
@scheduler.scheduled_job('cron', hour=15, minute=40)
@scheduler.scheduled_job('cron', hour=16, minute=40)
@scheduler.scheduled_job('cron', hour=17, minute=40)
@scheduler.scheduled_job('cron', hour=18, minute=40)
@scheduler.scheduled_job('cron', hour=19, minute=40)
@scheduler.scheduled_job('cron', hour=20, minute=40)
@scheduler.scheduled_job('cron', hour=21, minute=40)
@scheduler.scheduled_job('cron', hour=22, minute=40)
@scheduler.scheduled_job('cron', hour=23, minute=40)
@scheduler.scheduled_job('cron', hour=7, minute=55)
@scheduler.scheduled_job('cron', hour=8, minute=55)
@scheduler.scheduled_job('cron', hour=9, minute=55)
@scheduler.scheduled_job('cron', hour=10, minute=55)
@scheduler.scheduled_job('cron', hour=11, minute=55)
@scheduler.scheduled_job('cron', hour=12, minute=55)
@scheduler.scheduled_job('cron', hour=13, minute=55)
@scheduler.scheduled_job('cron', hour=14, minute=55)
@scheduler.scheduled_job('cron', hour=15, minute=55)
@scheduler.scheduled_job('cron', hour=16, minute=55)
@scheduler.scheduled_job('cron', hour=17, minute=55)
@scheduler.scheduled_job('cron', hour=18, minute=55)
@scheduler.scheduled_job('cron', hour=19, minute=55)
@scheduler.scheduled_job('cron', hour=20, minute=55)
@scheduler.scheduled_job('cron', hour=21, minute=55)
@scheduler.scheduled_job('cron', hour=22, minute=55)
@scheduler.scheduled_job('cron', hour=23, minute=55)
@scheduler.scheduled_job('cron', hour=0, minute=55)
# 到梦空间活动提醒
async def run_every_2_hour():
    updateConfiguration()
    bot = nonebot.get_bot()  # 获取botid
    data = activeQuery()
    if data[0] == 1:
        await bot.send_group_msg(group_id=qun, message=data[1])


# on_keyword()为针对命令型事件的响应，即以配置的命令前缀为开头的语句
# permission=SUPERUSER设置为该命令只对bot管理员响应，rule设置为只有私聊或者直接艾特bot时才会生效，priority设置执行优先级为10
sx = on_keyword(['hdsx', '/活动刷新'], permission=PRIVATE_FRIEND, priority=10)


@sx.handle()
async def jrrp_handle(bot: Bot, event: Event):
    data = activeQuery()
    if data[0] == 1:
        bot = nonebot.get_bot()  # 获取botid
        await bot.send_group_msg(group_id=qun, message=data[1])
        data = open('cj/到梦空间活动提醒/local.txt', encoding='utf-8')
        knownActivities = data.read()
        data.close()
        time.sleep(2)
        await sx.finish(knownActivities)
    else:
        await sx.finish('无活动更新')


inception_help = on_keyword(["/帮助"], rule=to_me(), priority=1)


@inception_help.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await inception_help.finish(Message("""现有模块帮助如下\n
关于 到梦空间活动提醒模块 帮助:
早7至晚12，每15分钟自动监测到梦空间新活动。\n
指令：
'/报名结果'|查询一次后销毁
'/更新主设备'|更新监测用的cookie和data
'/活动刷新'|提前检查是否有新活动
'/日志'   |获取上一条日志记录
'/关闭监测'|关闭监测活动
'/开启监测'|开启监测活动
\n注：有活动会发群里不需要手动获取\n
关于 到梦空间抢活动模块 帮助:
多线程并发执行报名请求包。\n
指令：
'/查看参数'|查看所有参数
'/清空参数'|清空所有参数
'/添改登陆参数'|新增用户或修改登陆参数
'/添加报名参数'|报名的包值
'/添加脚本参数'|时间参与者值
'/启动脚本'   |执行脚本
\n注：启动报名前建议关闭监测活动
    """))


registrationData = on_keyword(["bmjg", '/报名结果'], rule=to_me(), priority=2)


@registrationData.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    txt = open('cj/外部插件数据/抢活动结果.txt', encoding='utf-8')
    knownActivities = txt.read()
    txt.close()
    if knownActivities != '':
        txt = open('cj/外部插件数据/抢活动结果.txt', 'w', encoding='utf-8')
        txt.write('')
        txt.close()
    else:
        knownActivities = '近期没有可以查询的报名结果\n(查询一次后销毁)'
    await registrationData.finish(Message(knownActivities))


journal = on_keyword(["rz", '/日志'], permission=PRIVATE_FRIEND, priority=9)


@journal.handle()
async def journal_receive(bot: Bot, event: Event, state: T_State):
    fname = 'cj/到梦空间活动提醒/log.txt'
    with open(fname, 'r', encoding='utf-8') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        last_line = lines[-1][:3000]  # 取最后一行
    await journal.finish(last_line)


offMonitoring = on_keyword(["gbjc", '/关闭监测'], permission=PRIVATE_FRIEND, priority=9)


@offMonitoring.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    t = open('cj/到梦空间活动提醒/config.txt', 'w', encoding='utf-8')
    t.write('0')
    t.close()
    await offMonitoring.finish(Message('自动监测功能已经关闭'))


offMonitoring = on_keyword(["kqjc", '/开启监测'], permission=PRIVATE_FRIEND, priority=9)


@offMonitoring.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    t = open('cj/到梦空间活动提醒/config.txt', 'w', encoding='utf-8')
    t.write('1')
    t.close()
    await offMonitoring.finish(Message('自动监测功能已经开启'))
