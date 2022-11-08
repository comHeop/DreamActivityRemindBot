import time
import requests
import json

# 手机
sta = json.dumps({
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
})

headers = {
    'Cookie': '2f624a4616677875028367965e0e143623c093907579d2fd8453219fae425a',
    'Standardua': sta,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'DMKJ/4.4.7 (iPhone; iOS 16.0.2; Scale/3.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Content-Length': '894',
    'Connection': 'close'
}


def textWrite(path, data):
    t = open(path, 'w', encoding='utf-8')
    t.write(data)
    t.close()


def jpeg(jpeg):
    a = {
        "type": "image",
        "data": {
            "file": jpeg,
        }
    }
    return a


def text(text):
    b = {
        "type": "text",
        "data": {
            "text": text
        }
    }
    return b

def activeQuery():
    qun = []
    txt_s = ''
    # 信息获取参数
    data = 'd=eFRQYmd0K3dUUEdzUVpwVGU4VVV0MEtiUzZoS1M1MTBTUlFqQU1yY0k2Y3l5NGVqRnVxVUFEc012RG1GNkFZa3o1ejhNZmhhbDRBVlFKUFUvekgzemU1bTJweC8wN2Z3ZHpMaGFtM2djcHVMbmNtMWFqbTBQeTJKV2JKNXFuYzBPbVI0dXl1Zk1KZW5ycUJQWGVHRkFqR241WHZGem1YYXBYZmZXbmszb0VSbXE3a2ZONGI5V2ZEcEFTVE4vRkRrY0FMWWNEdldoS2hhVGxadUhRbEdDSHFvZXRXN2VOV2hWMzlpVjlBa2VZSldnRU1aLzRaNHdqN1BveUt2WFBiQnF2dVJSNFk5UUowNmNQeEFEdHoya0JqaW1zTEQ0UHBHUkpUTW9OQjNmeTJsY1JJTGR0T1ZEZlg0aE9TcnlMZkQxUU1vdW1INzZMT04xZy9mcW5YdTI2MVJxUGNqbWV2MytXRVg0NUZoWURnbUVRek03WmtuS3pXeWUwNFp3cXR2MXFyTHdKck1zZmNHVUg0NEQ0QW1hU3NSeG93VDc0UVphMnlFMk53L2phQzdnb2YwWXlGQWY3bGJqdm9KNU4yc3pLOUtRM2syVklTendFZDJiTGczMXBPRGlUY2VDVTlmSGhBOGdDV0VKZ2M9U1J0VGNPNWlGQ0syOUhuNlA1bnZQblRxdkllQjBUc010enhIVGc4Q0Vxd0YwMEhBc2ZqZk9IOTBvSHJXUU5OTW56Ui91N1AvbkoyQzdLM2s1aTA3QlZDY0FUYnlYVHdhbWVPaXZRK2h1YWlSak5wNUdWUnBYVGFSdUVkTHhyYkJudjFaL25pOGo5REdkZzlyY0R2R0hhY0FicXIvTlFpUFlJTDFZM25FNlA0PQ=='

    txt = open('cj/到梦空间活动提醒/config.txt', encoding='utf-8')
    switch = int(txt.read())
    txt.close()
    if switch == 1:
        # 测试用例
        # r = {'code': '100', 'data': {'haveMore': True, 'total': 0, 'list': [{'aid': '6376482', 'activityId': '6376482', 'imageUrl': 'https://image.5idream.net/41182015/1666593399699_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募县城路段巡视志愿者', 'status': '3', 'statusText': '报名中', 'activitytime': '2022.10.25 至 2022.10.25', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6367320', 'activityId': '6367320', 'imageUrl': 'https://image.5idream.net/41426259/1666531875059_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '初见·落叶留言活动', 'status': '3', 'statusText': '报名中', 'activitytime': '2022.10.25 至 2022.10.25', 'catalog2name': '技能特长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6363589', 'activityId': '6363589', 'imageUrl': 'https://image.5idream.net/35651504/1666507826183_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“中华优秀传统文化”主题借阅', 'status': '3', 'statusText': '报名中', 'activitytime': '2022.10.28 至 2022.10.30', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6362552', 'activityId': '6362552', 'imageUrl': 'https://image.5idream.net/41181943/1666500335873_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '食堂三楼生鲜窗口打卡', 'status': '3', 'statusText': '报名中', 'activitytime': '2022.10.25 至 2022.10.29', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6362514', 'activityId': '6362514', 'imageUrl': 'https://image.5idream.net/1231666584740850?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“七月流火，九月授衣”——寒衣节', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.24 至 2022.10.27', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6358360', 'activityId': '6358360', 'imageUrl': 'https://image.5idream.net/4063CB3F-0AC2-4135-9646-31F9C805A0C1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '二十四节气之霜降', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.23 至 2022.10.25', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6354769', 'activityId': '6354769', 'imageUrl': 'https://image.5idream.net/41152039/1666412822779_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '计算机系舞蹈队招募', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.22 至 2022.11.03', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6352249', 'activityId': '6352249', 'imageUrl': 'https://image.5idream.net/25EDADB7-9655-4336-B7AB-EF2F7A66D857?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '初霜渐冷', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.23 至 2022.10.25', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6322148', 'activityId': '6322148', 'imageUrl': 'https://image.5idream.net/F9AF8F95-8C8E-4D48-BB58-89C3DDAE2EFE?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '土木系加油稿征集活动', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.21 至 2022.10.31', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6308290', 'activityId': '6308290', 'imageUrl': 'https://image.5idream.net/41194020/1665983585693_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '校运会方块队', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.21 至 2022.11.03', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6303291', 'activityId': '6303291', 'imageUrl': 'https://image.5idream.net/41151089/1666021962583_4?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '计算机系第三十一届运动会方块队招募', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.18 至 2022.11.03', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6302924', 'activityId': '6302924', 'imageUrl': 'https://image.5idream.net/41086411/1666019548898_3?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '冶金系校运会方块队女生', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.20 至 2022.11.06', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6302869', 'activityId': '6302869', 'imageUrl': 'https://image.5idream.net/41086411/1666019195192_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '冶金系校运会方块队男生', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.20 至 2022.11.06', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6293999', 'activityId': '6293999', 'imageUrl': 'https://image.5idream.net/69EBABF2-0826-40FF-B7EB-5E194A7ECD06?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“喜迎二十大，书画颂党恩”软笔书法比赛', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.19 至 2022.11.01', 'catalog2name': '技能特长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6287323', 'activityId': '6287323', 'imageUrl': 'https://image.5idream.net/40975129/1665934913693_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '土木系三十一届校运会表演队招募', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.18 至 2022.11.03', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6287293', 'activityId': '6287293', 'imageUrl': 'https://image.5idream.net/40975129/1665934575503_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '土木系三十一届校运会方块队招募', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.18 至 2022.11.03', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6273365', 'activityId': '6273365', 'imageUrl': 'https://image.5idream.net/41181959/1665807823469_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '经管系校运会方块队招募', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.18 至 2022.11.03', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6246170', 'activityId': '6246170', 'imageUrl': 'https://image.5idream.net/35651504/1665552490461_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“共享金秋好时光”14天阅读打卡', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.13 至 2022.10.26', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6135712', 'activityId': '6135712', 'imageUrl': 'https://image.5idream.net/35651504/1664023052403_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '趣味阅读接龙', 'status': '5', 'statusText': '进行中', 'activitytime': '2022.10.19 至 2022.10.26', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6370680', 'activityId': '6370680', 'imageUrl': 'https://image.5idream.net/41181998/1666577811159_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募观众', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.24 至 2022.10.24', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6366031', 'activityId': '6366031', 'imageUrl': 'https://image.5idream.net/41181998/1666523775497_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募观众', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.24 至 2022.10.24', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6365998', 'activityId': '6365998', 'imageUrl': 'https://image.5idream.net/41194020/1666523250926_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招科技活动开幕式观众', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.24 至 2022.10.24', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6362910', 'activityId': '6362910', 'imageUrl': 'https://image.5idream.net/40928713/1666503068935_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募志愿者', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.23 至 2022.10.23', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6360383', 'activityId': '6360383', 'imageUrl': 'https://image.5idream.net/FDCF9710-AF43-4D7A-BB83-A12F2D929F61?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募志愿者', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.23 至 2022.10.23', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6359307', 'activityId': '6359307', 'imageUrl': 'https://image.5idream.net/40975129/1666448506947_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '六栋扫地活动', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.23 至 2022.10.23', 'catalog2name': '志愿公益', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6357312', 'activityId': '6357312', 'imageUrl': 'https://image.5idream.net/41182186/1666433314418_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '志愿者招募', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.23 至 2022.10.23', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6353105', 'activityId': '6353105', 'imageUrl': 'https://image.5idream.net/41426390/1666402412043_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '周末影院之《独行月球》', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.22 至 2022.10.22', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6344650', 'activityId': '6344650', 'imageUrl': 'https://image.5idream.net/41182015/1666324308184_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募志愿者', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.21 至 2022.10.21', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6329480', 'activityId': '6329480', 'imageUrl': 'https://image.5idream.net/41181998/1666154656828_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '到梦空间系统使用直播培训', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.21 至 2022.10.21', 'catalog2name': '创新创业', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6318939', 'activityId': '6318939', 'imageUrl': 'https://image.5idream.net/37877796/1666144658568_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '第三十一届田径体育运动会彩旗队', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.20 至 2022.10.20', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6318863', 'activityId': '6318863', 'imageUrl': 'https://image.5idream.net/37877796/1666143685364_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '第三十一届田径体育运动会鲜花队', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.20 至 2022.10.20', 'catalog2name': '文艺体育', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6308053', 'activityId': '6308053', 'imageUrl': 'https://image.5idream.net/41154135/1666068287268_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '追忆英雄，牢记历史', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.20 至 2022.10.22', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6307399', 'activityId': '6307399', 'imageUrl': 'https://image.5idream.net/40959037/1666066178813_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '献血知识问答活动', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.19 至 2022.10.21', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6306722', 'activityId': '6306722', 'imageUrl': 'https://image.5idream.net/E98B5315-D784-46F1-9805-7E502548F6F0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '第十三届社团活动月开幕式会旗展示志愿者招募', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.20 至 2022.10.24', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6303250', 'activityId': '6303250', 'imageUrl': 'https://image.5idream.net/40975167/1666021081040_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '献血小知识，你我共传递', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.19 至 2022.10.22', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6291506', 'activityId': '6291506', 'imageUrl': 'https://image.5idream.net/41194002/1665977721032_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '搬运物质', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.17 至 2022.10.17', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6283978', 'activityId': '6283978', 'imageUrl': 'https://image.5idream.net/41426390/1665916072117_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '招募志愿者', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.16 至 2022.10.16', 'catalog2name': '实践实习', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6281983', 'activityId': '6281983', 'imageUrl': 'https://image.5idream.net/35651504/1665904302112_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“红色经典”主题借阅', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.21 至 2022.10.24', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6278097', 'activityId': '6278097', 'imageUrl': 'https://image.5idream.net/41182015/1665879938198_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“青春献礼二十大  强国复兴有我”青年榜样分享会', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.16 至 2022.10.16', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}, {'aid': '6277673', 'activityId': '6277673', 'imageUrl': 'https://image.5idream.net/37935552/1665849112927_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg', 'name': '“青春献礼二十大，强国有我新征程”青马读书会主题活动', 'status': '6', 'statusText': '已结束', 'activitytime': '2022.10.16 至 2022.10.16', 'catalog2name': '思想成长', 'boutique': 0, 'boutiqueStr': ''}]}}
        r = requests.post(url='https://appdmkj.5idream.net/v2/activity/activities', headers=headers, data=data).json()
    else:
        return 0
    data = open('cj/到梦空间活动提醒/log.txt', 'a', encoding='utf-8')
    data.write(str(int(time.time())) + str(r) + '\n')
    data.close()
    txt = ''
    op = 0
    r = r['data']['list']
    data = open('cj/到梦空间活动提醒/data.txt', encoding='utf-8')
    knownActivities = data.read().split('\n')
    data.close()
    for i in r:
        data = open('cj/到梦空间活动提醒/data.txt', 'a', encoding='utf-8')
        pd = 0
        for u in knownActivities:
            if u != '':
                if i['activityId'] == u:
                    pd = 0
                    break
                else:
                    pd = 1
        if pd == 1:
            data.write(i['activityId'] + '\n')
            txt = (i['name'] + '\n报名详情：' + i['statusText'])
            txt_s += txt
            qun.append(jpeg(i['imageUrl']))
            qun.append(text(txt))
            op = 1
        data.close()
    if op == 0:
        textWrite('cj/到梦空间活动提醒/local.txt', '无活动更新')
    else:
        t = open('cj/到梦空间活动提醒/local.txt', 'w', encoding='utf-8')
        t.write('活动提醒\n' + txt_s)
        t.close()
    data.close()

    return op, qun
