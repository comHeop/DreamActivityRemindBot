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
             "screenResolution": "900-1600",
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
    }]


class parameter:
    # 登陆参数
    login_s = {
        '王秀旭': 'd=ZHJRei9lOEc3RnJYZ1YyaEI2aXZ3LzE5SzJaSEMxWWYxY0R4cUZ3aTllZ1ZzNGkzZCtiVXRGaTVhZlNFSFJQQXNudEgxOXBiWUYrZGN4RFVtUlhnK1dMR1hNaWpObWxGN2RPQWZaY0hiYS9PY2VmYnUrcEVzUm9RWU5IV2NXMlcwT3M5Q095b1pVNlV3akhTaHJvL1dPZ0I5d2UvMXRMOGlWUXlrRWFGbTFTaU5HTFhKWG5NaVZ1TXM5dHMrVm14RWhERWU3OFoxVko4VnRhblhKTXRxdz09TVFDSFdKTDdMNDhmRlVDQ3BKV1dwT21uVWZmVnNobkN5OXoxcXQ3dm8rczcyWlN1TVhxVlFBVElMRXp2Q3VvSFB1aXBnbVkyVjJzTEJLNUxTdjhiMFd5SDc4SnBibGw5M2dXQjkySXJFelMwYlF2WVhGVjdXa0RQVm5tdXlnNWVsUUZoVkNJREphS3JidGVPakMvSjhvVTFzU3ExWUtzd3dXMzBKUFUwSGlBPQ%3D%3D',
        '巫鑫': 'd=YTF5K1V5aU9ubDhERU9Rb3VYd1VwSlhIUFlPUG5NYm9jYWVwTTMvNXdsWDhoV29mc2dWaDhlanl4L2svRS82NktJTy9Eb0YzSkFHKzRROUxUWTJGRDlxTG9IYmpxRHQ1OU9KeUhkNzZ5R3I1dkh5MFMvTG9OSTBFWm5odzJ4cGVzbXpYRDdiaUQ5WGtVaGtHZkFuNC9qOXYwd1N3dmR3VTQ3ZDZNKzNjdS9xRng4MlFqdUVJdWEwc29adXVhZ2pIeE9RUzQ3U25LYjZ3cGNwcjBOYVJBQT09SEpteE9TVlRRZU9FVlF2SGxJeEpyczdKem8rQjNvMlJjajc1cU0wMjVEZ1ZMMzdjajZnbmpMVUFCSjVhQzh5TkRicGh5NVcraHhJL1dTS3FUL3ZNazUyR28rdERkQUlWN0FvcUFnU3Q0R2M3RGlKR0plR2dPcDdoeUpKUy95cjQ3TnF5ekxWKzRkblJDTUljbTVacXhvRW9RWWk3cGFrV1NNN3kvOERuYklNPQ%3D%3D',
        '唐秀厅': 'd=N2ZZQ05qNzlLTmRDU2llbEJXSFRuQTVRN1F1WkVMVzVjMjBUZ1drd3ZKZThNQ3FQYUN4SnRIWG91TzVQczd3OXNRRVp1N1RhTWlqRHVqTjkxQTJ1NVA1ZXdsYURlVUZuMDg3TmppWjhRS0VCakhjdkxwc1licHdqeFRBb1Z6cmh1TldqcUFQYVRCNHZsejIrMFlEbHJXQzNIKzZCczNOeUV1d0t5U1NSS0F1amRWQjlMTVhUT3F2RWVKeHNhalFQb251UmdFQ09SbExGNjVBNUdKQStxUT09TlY2Qm9OakRnaWlFWWhsejdyZlQ5OGZGa3I1K2ptWTdXcjcrSkFndFBERjl1MWRjL3VCYitlZTA0d2k3NVNUM2lxWGYvT2VtaHBFQ2dYVG1TdkphSmdyeVhPUlFUMnRxcHd0aE1XeGQzRmthZEROZW92N0lKMDc5bVJ5VlltRGFoK1BjSGJvVTV5NXRLdGlXMG1iN1BGRXhIMGZMdUFXc3RBVU5NM1FQY3ZNPQ%3D%3D'
    }
    # 报名参数
    signUp_data_s = {
        '王秀旭': '000',
        '巫鑫': '000',
        '唐秀厅': '000',
        '杨洪权': '000'
    }


class startUp:
    name = ''
    time = ''


# 更新报名参数
for name in os.listdir('cj/到梦空间抢活动/数据'):
    with open('cj/到梦空间抢活动/数据/' + name, encoding='utf-8') as file:
        content = file.read()
        if content != '':
            dataList = re.split(',', content)
            parameter.signUp_data_s[dataList[0]] = dataList[1]
        else:
            continue
