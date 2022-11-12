import json
import os
import re
import time


class phoneID:
    # 手机
    headers_Apple = {
        'Cookie': '2f624a4416673955121362493e32ef3edd100eff7f8774797afb2cb8944268',
        'Standardua': json.dumps({
            "uuid": "678b0e7592a8489898c8b7ee8a45c6a3",
            "system": "iOS",
            "version": "4.4.7",
            "sysVersion": "16.0.2",
            "screenResolution": "1125.000000-2436.000000",
            "JPushId": "678b0e7592a8489898c8b7ee8a45c6a3",
            "countryCode": "CN",
            "channelName": "dmkj_iOS",
            "createTime": "0",
            "operator": "%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A146011",
            "modifyTime": "0",
            "device": "iPhone13,2",
            "hardware": "D53gAP,iPhone13,2,arm64,127870980096,-445497344",
            "startTime": str(int(time.time()))
        }),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'DMKJ/4.4.7 (iPhone; iOS 16.0.2; Scale/3.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Content-Length': '894',
        'Connection': 'close'
    }
    headers_Android = [{
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1666416798936',
            "device": "Xiaomi M2007J22C",
            "hardware": "qcom",
            "jPushId": "190e35f7e0af018ab4f",
            "modifyTime": '1666416798936',
            "operator": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
            "screenResolution": "900-1600",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 25 7.1.2",
            "system": "android",
            "uuid": "080027333A0F",
            "version": "4.4.7"}
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '554',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.11.0',
        'Connection': 'close'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1666776342256',
            "device": "samsung SM-G955N",
            "hardware": "samsungexynox8895",
            "jPushId": "",
            "modifyTime": '1666776342256',
            "operator": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
            "screenResolution": "720-1280",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 25 7.1.2",
            "system": "android",
            "uuid": "0800270676FA",
            "version": "4.4.7"}
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '554',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.11.0',
        'Connection': 'close'
    }, {
        'Standardua': json.dumps(
            {"channelName": "dmkj_Android",
             "countryCode": "CN",
             "createTime": '1666778403374',
             "device": "samsung SM-G955N",
             "hardware": "samsungexynox8895",
             "jPushId": "",
             "modifyTime": '1666778403374',
             "operator": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
             "screenResolution": "720-1280",
             "startTime": str(int(round(time.time() * 1000))),
             "sysVersion": "Android 22 5.1.1",
             "system": "android",
             "uuid": "354730374374423",
             "version": "4.4.7"}
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '554',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.11.0',
        'Connection': 'close'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1666416186452',
            "device": "samsung SM-G10",
            "hardware": "samsungexynox",
            "jPushId": "190e35f7e0af018ab4f",
            "modifyTime": '1666416798936',
            "operator": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
            "screenResolution": "900-1600",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 25 7.1.2",
            "system": "android",
            "uuid": "080027043A0F",
            "version": "4.4.7"}
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '554',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.11.0',
        'Connection': 'close'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1666416186452',
            "device": "samsung",
            "hardware": "samsungexynox",
            "jPushId": "190e35f7e0af018ab4f",
            "modifyTime": '1666416698745',
            "operator": "%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8",
            "screenResolution": "1600-900",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 25 7.1.2",
            "system": "android",
            "uuid": "080027343A0F",
            "version": "4.4.7"}
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '554',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.11.0',
        'Connection': 'close'
    }]


class parameter:
    # 登陆参数
    login_s = {}
    # 报名参数
    signUp_data_s = {}


class startUp:
    name = ''
    time = ''


def updateConfiguration():
    # 更新报名参数
    for name in os.listdir('cj/到梦空间抢活动/数据/login'):
        with open('cj/到梦空间抢活动/数据/' + name, encoding='utf-8') as file:
            content = file.read()
            if content != '':
                dataList = re.split(',', content)
                parameter.signUp_data_s[dataList[0]] = 'd=' + dataList[1]
            else:
                continue

    # 更新登陆参数
    for name in os.listdir('cj/到梦空间抢活动/数据/login'):
        with open('cj/到梦空间抢活动/数据/login/' + name, encoding='utf-8') as file:
            content = file.read()
            if content != '':
                parameter.login_s[name.replace('.txt', '')] = 'd=' + content
                file.close()
            else:
                continue

    with open('cj/到梦空间活动提醒/cookieData.txt', 'r') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        if lines != "":
            first_line = lines[0]  # 取第一行
            phoneID.headers_Apple['Cookie'] = 'acw_tc=' + first_line.replace('\n', '')


updateConfiguration()
