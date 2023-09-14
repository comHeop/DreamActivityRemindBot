import nonebot
from nonebot import require
import time

from nonebot.adapters.onebot.v11 import PRIVATE_FRIEND
from nonebot.internal.params import ArgPlainText
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters import Event
from nonebot.rule import to_me
from cj.dream_remind.method import activeQuery, schoolQuery, dDataUp, closeDataUp, text

scheduler = require('nonebot_plugin_apscheduler').scheduler

minute = "5"  # 查询的间隔时间(分钟)
hour = "7-23"  # 查询的时间段(24小时制)


@scheduler.scheduled_job('cron', minute='*/%s' % minute, hour='%s' % hour)
async def run_every_2_hour():
    schoolData = schoolQuery(True, "0")
    if not schoolData['error']:
        for s in schoolData['uuid']:
            bot = nonebot.get_bot()  # 获取botid
            data = activeQuery(s)
            if data['error']:
                if data['msg'] != '活动更新已被禁用':
                    await bot.send_msg(message_type='private', user_id=data['admin'], message=[text(data['msg'])])
            else:
                if len(data['msg']) != 0:
                    for qun in data['qqGroup']:
                        await bot.send_group_msg(group_id=qun, message=data['msg'])
                        time.sleep(5)


# on_keyword()为针对命令型事件的响应，即以配置的命令前缀为开头的语句
# permission=SUPERUSER设置为该命令只对bot管理员响应，rule设置为只有私聊或者直接艾特bot时才会生效，priority设置执行优先级为10
sx = on_keyword(['renew', '/活动刷新'], permission=PRIVATE_FRIEND, priority=10)


@sx.handle()
async def jrrp_handle(event: Event):
    schoolData = schoolQuery(False, event.get_user_id())
    if not schoolData['error']:
        bot = nonebot.get_bot()
        data = activeQuery(schoolData['uuid'])
        if data['error']:
            await bot.send_msg(message_type='private', user_id=data['admin'], message=[text(data['msg'])])
        else:
            if len(data['msg']) != 0:
                await bot.send_msg(message_type='private', user_id=data['admin'], message=[text("已经获取到新活动")])
                for qun in data['qqGroup']:
                    await bot.send_group_msg(group_id=qun, message=data['msg'])
                    time.sleep(5)
            else:
                await bot.send_msg(message_type='private', user_id=data['admin'], message=[text("暂无新活动")])


inception_help = on_keyword(['bz', "/帮助"], rule=to_me(), priority=1)


@inception_help.handle()
async def handle_first_receive():
    await inception_help.finish(Message("""
帮助:
监控频率 %s 分钟，时段 %s
指令：
'bz,/帮助'：帮助
'renew,/活动刷新': 手动提前刷新活动
'update,/更新参数': 更新参数d的值
'onoff,/监测': 停止/开启,当前的监测
""" % (minute, hour)))


update = on_keyword(['update', '/更新参数'], permission=PRIVATE_FRIEND, priority=2)


@update.got('city', prompt='请直接输入不带参数,不要带"d=",不要进行任何转义')
async def _(event: Event, ity: str = ArgPlainText('city')):
    data = dDataUp(ity, event.get_user_id())
    if not data['error']:
        await update.finish('参数更新成功！')
    else:
        await update.finish('更新失败' + data['msg'])


onoff = on_keyword(['onoff', '/监测'], permission=PRIVATE_FRIEND, priority=2)


@onoff.handle()
async def onoff(event: Event):
    bot = nonebot.get_bot()
    data = closeDataUp(event.get_user_id())
    if not data['error']:
        await bot.send_msg(message_type='private', user_id=event.get_user_id(), message=[text(data['msg'])])
    else:
        await bot.send_msg(message_type='private', user_id=event.get_user_id(), message=[text('更新失败, ' + data['msg'])])
