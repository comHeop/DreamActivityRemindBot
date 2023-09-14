import requests

domainNames = 'https://api.dream.gllg.cc'   # 后端域名


def jpeg(j):
    """
    图片格式化
    :param j: data
    :return: {...a}
    """
    a = {
        "type": "image",
        "data": {
            "file": j,
        }
    }
    return a


def text(t):
    """
    文本格式化
    :param t: data
    :return: {...t}
    """
    b = {
        "type": "text",
        "data": {
            "text": t
        }
    }
    return b


def schoolQuery(schoolQ: bool, qq: str):
    """
    查询全学校id与qq号反查
    :param schoolQ: true全学校id，false反查
    :param qq: 管理员qq号
    :return: res -见后端接口注解
    """
    if schoolQ:
        url = "%s/dreamActivityApi/query.php" % domainNames
        r = requests.get(url).json()
        return r
    else:
        url = "%s/dreamActivityApi/query.php" % domainNames
        data = {
            "admin": qq,
        }
        r = requests.get(url, params=data).json()
        return r


def activeQuery(schoolId: int):
    """
    活动更新检查
    :param schoolId: 学校id
    :return: error，admin管理员qq号，msg活动数据，qqGroup群号
    """
    message = []
    url = "%s/dreamActivityApi" % domainNames
    data = {
        "schoolId": schoolId,
    }
    r = requests.get(url, params=data).json()
    if r['error']:
        return {
            'error': True,
            'admin': r['admin'],
            'msg': r['msg'],
        }
    # 检查是否有新活动
    if len(r['msg']) != 0:
        for i in r['msg']:
            txt = (i['name'] + '\n活动：' + i['statusText'] + '\n活动时间：' + i['activitytime'] + '\n类型：' + i[
                'catalog2name'] + '\n级别：' + i['boutiqueStr'])
            message.append(jpeg(i['imageUrl']))
            message.append(text(txt))
    return {
        'error': False,
        'qqGroup': r['qqGroup'],
        'msg': message,
        'admin': r['admin'],
    }


def dDataUp(d: str, qq: str):
    """
    d参数更新
    :param d: 参数内容
    :param qq: 管理员qq号
    :return: res -见后端接口注解
    """
    url = "%s/dreamActivityApi/modify.php" % domainNames
    data = {
        "admin": qq,
        "d": d,
    }
    r = requests.get(url, params=data).json()
    return r


def closeDataUp(qq: str):
    """
    关闭更新
    :param qq: 管理员qq号
    :return: res -见后端接口注解
    """
    url = "%s/dreamActivityApi/modify.php" % domainNames
    data = {
        "admin": qq,
        "close": 'a',
    }
    r = requests.get(url, params=data).json()
    return r
