import json
import os
import re
import time


class phoneID:
    # 手机
    headers_Apple = {
        'Cookie': '2f624a4416673955121362493e32ef3edd100eff7f8774797afb2cb8944268',
        'standardUA': json.dumps({
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
        'Host': 'appdmkj.5idream.net',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'DMKJ/4.4.7 (iPhone; iOS 16.0.2; Scale/3.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Content-Length': '894',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    headers_Android = [{
        'standardUA': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "Sony H9493",
            "hardware": "qcom",
            "jPushId": "1507bfd3f72c6850f06",
            "modifyTime": '1669122025036',
            "operator": "%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 9",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '605',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "vivo V2020A",
            "hardware": "V2020A",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 10",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "Xiaomi Redmi K30",
            "hardware": "Redmi K30",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 8.0",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "vivo V1829A",
            "hardware": "V1829A",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 8.0",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "HUAWEI AKA-AL10",
            "hardware": "AKA-AL10",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 10",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "samsung SM-G9500",
            "hardware": "SM-G9500",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 7.1",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }, {
        'Standardua': json.dumps({
            "channelName": "dmkj_Android",
            "countryCode": "CN",
            "createTime": '1669118437742',
            "device": "QIKU 8676-M01",
            "hardware": "8676-M01",
            "jPushId": "",
            "modifyTime": '1669122025036',
            "operator": "%E6%9C%AA%E7%9F%A5",
            "screenResolution": "1440-2696",
            "startTime": str(int(round(time.time() * 1000))),
            "sysVersion": "Android 28 11",
            "system": "android",
            "uuid": "38786286573C",
            "version": "4.4.7"
        }
        ),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '940',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }]


class parameter:
    # 登陆参数
    login_s = {
        '杨洪权': '555',
        '巫鑫': '000',
        '唐秀厅': '999'
    }
    # 报名参数
    signUp_data_s = {'杨洪权': '555',
                     '巫鑫': '000',
                     '唐秀厅': '999'}


class startUp:
    name = ''
    time = ''


def updateConfiguration():
    # 更新报名参数
    for name in os.listdir('cj/到梦空间抢活动/数据/login'):
        with open('cj/到梦空间抢活动/数据/' + name, encoding='utf-8') as file:
            content = file.read()
            if ',' in content:
                dataList = re.split(',', content)
                parameter.signUp_data_s[dataList[0]] = 'd=' + dataList[1]
            else:
                continue

    # 更新登陆参数
    for name in os.listdir('cj/到梦空间抢活动/数据/login'):
        with open('cj/到梦空间抢活动/数据/login/' + name, encoding='utf-8') as file:
            content = file.read()
            if ',' in content:
                parameter.login_s[name.replace('.txt', '')] = 'd=' + content
                file.close()
            else:
                continue

    with open('cj/到梦空间活动提醒/cookieData.txt', 'r') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        if not lines:
            lines = ['0']
        first_line = lines[0]  # 取第一行
        phoneID.headers_Apple['Cookie'] = 'acw_tc=' + first_line.replace('\n', '')

# updateConfiguration()
