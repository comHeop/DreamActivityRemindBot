import time
import pymysql
import os
import shutil

host = 'localhost'
user = 'root'
password = 'e234e7ccbfd6a1ec'
database = 'qryhqkim'

"""
7447503  篮球争霸赛招募啦啦队观众  2023.03.29
[{'name': '篮球争霸赛招募啦啦队观众', 'start_time': '2023.03.29', 'end_time': '2023.03.29', 'hd_id': '7447503'}]

7446571  重温百年党史，践行初心使命  2023.03.31
[{'name': '重温百年党史，践行初心使命', 'start_time': '2023.03.31', 'end_time': '2023.04.04', 'hd_id': '7446571'}]
"""


def informationWriteSql(info_list):
    """
    SQL数据写入
    :param info_list:活动信息列表(外数组内字典)
    :return:SQL结果
    """
    myconn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
    mycursor = myconn.cursor()  # 创建游标对象

    sql = 'INSERT INTO `hdxx`(`name`, `start_time`, `end_time`, `hd_id`) VALUES (%s,%s,%s,%s)'
    for player in info_list:
        # 将 时间字符串 转换成 结构化时间 用于过度
        player['start_time'] = player['start_time'] + ' 00:00:00'
        player['end_time'] = player['end_time'] + ' 00:00:00'
        # mktime()，将 结构化时间 转换为 时间戳
        start_time = time.mktime(time.strptime(player['start_time'], '%Y.%m.%d %H:%M:%S'))
        end_time = time.mktime(time.strptime(player['end_time'], '%Y.%m.%d %H:%M:%S'))
        # 执行SQL
        myconn.ping(reconnect=True)
        mycursor.execute(sql, (player['name'], int(start_time), int(end_time), player['hd_id']))
    myconn.commit()  # 存储游标结果
    mycursor.close()  # 关闭连接
    return mycursor.rowcount


def pastActivitiesDeleteSql():
    """
    清理已经结束的活动的signkey
    :return: 0
    """
    myconn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
    now_time = int(time.time()) + 86400000
    mycursor = myconn.cursor()  # 创建游标对象
    sql = 'DELETE FROM `hdxx` WHERE `end_time` < %s'
    mycursor.execute(sql, now_time)
    myconn.commit()  # 存储游标结果
    mycursor.close()  # 关闭连接
    return 0


def createHtml(hdid, name, start_time):
    """
    建立指定活动id的网页文件
    :param hdid: 活动id
    :param name: 活动名称
    :param start_time: 结束时间。例：2022.10.16
    :return: 0
    """
    src_dir = '/www/wwwroot/qr.yhq.kim/hdqd/demo/index.html'  # 复制的文件
    dst_dir = '/www/wwwroot/qr.yhq.kim/hdqd/%s/' % hdid  # 目的路径记得加斜杠
    os.makedirs(dst_dir)  # 新建文件夹
    cwd = os.getcwd()
    os.chdir(cwd)
    filename = dst_dir + 'index.html'
    with open(os.path.join(cwd, filename), 'wb') as f:
        str = ''
        str = str.encode()
        f.write(str)
    os.chmod(filename, 1005)  # 对应宝塔775权限
    in_file = open(src_dir, "r", encoding='utf8')
    out_file = open(dst_dir + 'index.html', "w", encoding='utf8')
    lines = in_file.readlines()
    for ips in lines:
        ips = ips.replace("'&%hdmc&%'", name).replace("&%kssj&%", start_time.replace('.', '-'))
        out_file.write(ips)
    in_file.close()
    out_file.close()
    return 0


def del_file(path):
    """
    递归清空文件夹内所有东西后删除文件夹
    :param path:路径
    :return:0
    """
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):  # 如果是文件夹那么递归调用一下
            del_file(c_path)
        else:  # 如果是一个文件那么直接删除
            os.remove(c_path)
    shutil.rmtree(path)  # 删除文件夹
    return 0


def deleteOutOfDateHtml():
    """
    清理已经结束的活动的html
    :return: 0
    """
    myconn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
    now_time = int(time.time()) + 86400000
    mycursor = myconn.cursor()  # 创建游标对象
    sql = 'SELECT `hd_id` FROM `hdxx` WHERE `end_time` < %s'
    mycursor.execute(sql, now_time)
    results = mycursor.fetchall()
    result = []
    for row in results:
        result.append(row[0])
    if len(result) != 0:
        for hdid in result:
            del_file('/www/wwwroot/qr.yhq.kim/hdqd/%s/' % hdid)
    mycursor.close()  # 关闭连接
    return 0


def activityStatistics():
    """
    统计已有的活动信息
    :return: 0
    """
    myconn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
    mycursor = myconn.cursor()  # 创建游标对象
    sql = 'SELECT hdxx.name, hdxx.hd_id, COUNT(dmkjsignkey.hd_id) AS repeat_count FROM hdxx LEFT JOIN dmkjsignkey ON hdxx.hd_id = dmkjsignkey.hd_id GROUP BY hdxx.name, hdxx.hd_id ORDER BY repeat_count DESC;'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    result = []
    for row in results:
        resultjson = {
            "name": row[0],
            "id": row[1],
            "count": row[2]
        }
        result.append(resultjson)
    mycursor.close()  # 关闭连接
    with open('/www/wwwroot/qr.yhq.kim/ActivityStatistics.txt', 'w') as f:
        f.write(str(result))
    return 0
