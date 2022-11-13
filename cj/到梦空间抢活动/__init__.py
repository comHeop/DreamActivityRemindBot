import os
import re
import time

from nonebot.plugin import on_keyword
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, PRIVATE_FRIEND
from nonebot.rule import to_me

from cj.到梦空间抢活动.Active_robbery import activeRobberyMain, dataEliminate
from cj.到梦空间抢活动.config import updateConfiguration

wettr = on_keyword(['tjbmcs', '/添加报名参数'], permission=PRIVATE_FRIEND, priority=2)


@wettr.handle()
async def _handle(matcher: Matcher, city: Message = CommandArg()):
    if city.extract_plain_text() and city.extract_plain_text()[0] != '_':
        matcher.set_arg('city', city)


@wettr.got('city', prompt='格式如下：名称#报名参数')
async def _(city: str = ArgPlainText('city')):
    it = re.search(r".*#.*", city)
    if it is not None:
        parameterList = re.split('#', it.group())
        if parameterList[0] + '.txt' in os.listdir('cj/到梦空间抢活动/数据/login'):
            txt = open('cj/到梦空间抢活动/数据/' + parameterList[0] + '.txt', 'w', encoding='utf-8')
            txt.write(parameterList[0] + "," + parameterList[1])
            txt.close()
            await wettr.finish('%s 的 报名 参数添加成功！' % (parameterList[0]))
        else:
            await wettr.finish('没有名为 %s 的用户。添加败！' % (parameterList[0]))
    else:
        await wettr.finish('输入不合法！请重新输入！')


ckbmcs = on_keyword(["ckcs", '/查看参数'], rule=to_me(), priority=8)


@ckbmcs.handle()
async def journal_receive():
    content = ''
    for name in os.listdir('cj/到梦空间抢活动/数据'):
        if re.search(r".*txt", name):
            with open('cj/到梦空间抢活动/数据/' + name, encoding='utf-8') as file:
                content += file.read()[:50] + '\n'
    with open('cj/到梦空间抢活动/data.txt', encoding='utf-8') as file:
        content_2 = file.read()
        if content_2 != '':
            content_2 = re.split('\n', content_2)
        else:
            content_2 = ['', '']
    await ckbmcs.finish('执行时间：%s\n参与者：%s\n报名参数\n%s' % (content_2[0], content_2[1], content))


qkbmcs = on_keyword(["qkcs", '/清空参数'], permission=PRIVATE_FRIEND, priority=9)


@qkbmcs.handle()
async def journal_receive():
    dataEliminate()
    await qkbmcs.finish('参数已全部清空。')


tjjbcs = on_keyword(['tjjbcs', '/添加脚本参数'], permission=PRIVATE_FRIEND, priority=2)


@tjjbcs.handle()
async def _handle(matcher: Matcher, qd: Message = CommandArg()):
    if qd.extract_plain_text() and qd.extract_plain_text()[0] != '_':
        matcher.set_arg('qd', qd)


@tjjbcs.got('qd', prompt='活动开始时间\n(例如格式：2022-10-28 14:35:00)')
async def _(qd: str = ArgPlainText('qd')):
    try:
        times_s = time.strptime(qd, '%Y-%m-%d %H:%M:%S')
        times_s = time.mktime(times_s)
        if time.time() - times_s > 0:
            await tjjbcs.finish('输入的时间小于当前时间，请检查后重试。')
    except:
        await tjjbcs.finish('输入的时间格式有误请检查。')


@tjjbcs.got('names', prompt='参与报名的用户\n(例如格式：王**,唐**,...)')
async def _(qd: str = ArgPlainText('qd'), namesa: str = ArgPlainText('names')):
    names = re.split(',', namesa + ',')
    names.pop(-1)
    for name in names:
        try:
            if open('cj/到梦空间抢活动/数据/login/' + name + '.txt', encoding='utf-8').read() != "":
                with open('cj/到梦空间抢活动/数据/' + name + '.txt', encoding='utf-8') as file:
                    content = file.read()
                    if content == "":
                        await tjjbcs.finish('没有查到 ' + name + ' 的 报名 参数，请检查。')
            else:
                await tjjbcs.finish('没有查到 ' + name + ' 的 登陆 参数，请检查。')
        except:
            await tjjbcs.finish('没有查到 ' + name + ' 这个用户，请检查。')
    txt = open('cj/到梦空间抢活动/data.txt', 'w', encoding='utf-8')
    txt.write('%s\n%s' % (qd, namesa))
    txt.close()
    await tjjbcs.finish('脚本参数添加成功！')


qdjb = on_keyword(['qdjb', '/启动脚本'], permission=PRIVATE_FRIEND, priority=2)


@qdjb.handle()
async def _qdjb():
    updateConfiguration()
    with open('cj/到梦空间抢活动/data.txt', encoding='utf-8') as file:
        qdNames = file.read()
    qdNames = re.split('\n', qdNames)
    names = re.split(',', qdNames[1] + ',')
    names.pop(-1)
    qd = qdNames[0]
    result = activeRobberyMain(qd, names)
    dataEliminate()
    await qdjb.finish(result)


gxzsb = on_keyword(['gxzsb', '/更新主设备'], permission=PRIVATE_FRIEND, priority=2)


@gxzsb.handle()
async def _handle(matcher: Matcher, ity: Message = CommandArg()):
    if ity.extract_plain_text() and ity.extract_plain_text()[0] != '_':
        matcher.set_arg('city', ity)


@gxzsb.got('city', prompt='格式如下：cookie#d')
async def _(ity: str = ArgPlainText('city')):
    it = re.search(r".*#.*", ity)
    if it is not None:
        parameterList = re.split('#', it.group())
        txt = open('cj/到梦空间活动提醒/cookieData.txt', 'w', encoding='utf-8')
        txt.write(parameterList[0] + "\n" + parameterList[1])
        txt.close()
        await gxzsb.finish('参数修改成功！')
    else:
        await gxzsb.finish('输入不合法！请重新输入！')


tjyh = on_keyword(['zgdlcs', '/添改登陆参数'], permission=PRIVATE_FRIEND, priority=2)


@tjyh.handle()
async def _handle(matcher: Matcher, ity: Message = CommandArg()):
    if ity.extract_plain_text() and ity.extract_plain_text()[0] != '_':
        matcher.set_arg('city', ity)


@tjyh.got('city', prompt='格式如下：名称#登陆参数')
async def _(ity: str = ArgPlainText('city')):
    it = re.search(r".*#.*", ity)
    if it is not None:
        parameterList = re.split('#', it.group())
        txt = open('cj/到梦空间抢活动/数据/login/' + parameterList[0] + '.txt', 'w', encoding='utf-8')
        txt.write(parameterList[1])
        txt.close()
        txt = open('cj/到梦空间抢活动/数据/' + parameterList[0] + '.txt', 'w', encoding='utf-8')
        txt.write(parameterList[1])
        txt.close()
        await tjyh.finish('成功！')
    else:
        await tjyh.finish('输入不合法！请重新输入！')
