import os
import re
import sys
import threading

import pymysql
import requests
import time
from cj.到梦空间抢活动.config import parameter, phoneID

host = 'localhost'
user = 'root'
password = 'e234e7ccbfd6a1ec'
database = 'qryhqkim'


def signkeyDeleteSql(hdid):
    """
    删除指定活动的signkey
    :param hdid: 活动id
    :return: 0
    """
    myconn = pymysql.connect(host=host, user=user, password=password, database=database,
                             charset='utf8')
    mycursor = myconn.cursor()  # 创建游标对象

    sql = 'DELETE FROM `dmkjsignkey` WHERE `hd_id`= %s'
    mycursor.execute(sql, hdid)
    myconn.commit()  # 存储游标结果
    return 0


def login(data, n, headers):
    # r = {'code': '100', 'data': {'getResult': True, 'signUpId': '3_6353105_45057137'}}  # 本地测试用例
    r = requests.post(url='https://appdmkj.5idream.net/v2/login/phone', headers=headers, data=data).json()
    if r['code'] == '100':
        login_values.append([str(n) + ' ：' + ' !!模拟登陆成功!!' + '\n',
                             str(int(time.time())) + str(n) + '抢活动脚本 ' + ' !!模拟登陆成功!!' + str(r) + '\n'])
        return True
    else:
        login_values.append([str(n) + ' ：' + ' ??模拟登陆失败??' + '\n',
                             str(int(time.time())) + str(n) + '抢活动脚本 ' + ' ??模拟登陆失败??' + str(r) + '\n'])
        return False


def signUp(data, n, headers):
    # r = {'code': '200', 'data': {'getResult': True, 'signUpId': '3_6353105_45057137'}}      # 本地测试用例
    r = requests.post(url='https://appdmkj.5idream.net/v2/signup/submit', headers=headers, data=data).json()
    # 判断返回结果
    if r['code'] == '100':
        signUp_values.append([str(n) + ' ：' + ' !!活动报名成功!!' + '\n',
                              str(int(time.time())) + str(n) + '抢活动脚本 ' + ' !!活动报名成功!!' + str(r) + '\n'])
    else:
        signUp_values.append([str(n) + ' ：' + ' ??活动报名失败??' + '\n',
                              str(int(time.time())) + str(n) + '抢活动脚本 ' + ' ??活动报名失败??' + str(r) + '\n'])


def log_seva(datas, n):
    # 日志存储
    for data in datas:
        txt = open('cj/到梦空间活动提醒/log.txt', 'a', encoding='utf-8')
        txt.write(data[n])
        txt.close()


def concurrency_signUp(data, n, headers):
    # 针对函数创建线程，target为调用的并发函数，args为调用函数的参数，该参数必须为数组否则运行会报错
    t = threading.Thread(target=signUp, args=(data, n, headers))
    threads.append(t)  # 添加线程到线程组


def activeRobberyMain(times, names):
    global threads, login_values, signUp_values
    # 全局变量收集多线程返回值
    signUp_values = []
    login_values = []
    threads = []  # 创建一个进程池
    # 检查是否大于当前日期
    times_s = time.strptime(times, '%Y-%m-%d %H:%M:%S')
    times_s = time.mktime(times_s)
    if time.time() - times_s > 0:
        return '输入的时间小于当前日期，请检查后重试。'
    # 模拟登陆
    blist = []
    for j in range(len(names)):
        blist.append(names[j])
    try:
        blist.remove('杨洪权')
    except:
        print('')
    if blist != '':
        print('\n开始执行模拟登陆，预计 %s 秒后完成\n' % (str((len(blist) + 1) * 2)))
        time.sleep(1)
        num = 0
        loginResult_x = 0
        for name in blist:
            headers = phoneID.headers_Android[num]
            a = parameter.login_s[name]
            loginResult = login(a, name, headers)  # 判断登陆结果
            if not loginResult:
                loginResult_x = 1
            print(login_values[num][0])
            time.sleep(2)
            num += 1
        # log_seva(login_values, 1)  # 登陆结果储存进日志
        if loginResult_x == 1:
            return '有用户登陆失败，取消执行。详情见日志。'
    else:
        print('\n无需模拟登陆\n')
    # 创建并发报名请求
    num = 0
    for name in names:
        a = parameter.signUp_data_s[name]
        if name == '杨洪权':
            headers = phoneID.headers_Apple
        else:
            headers = phoneID.headers_Android[num]
            num += 1
        concurrency_signUp(a, name, headers)
    # 等待时间开始
    while True:
        times_sa = time.strptime(times, '%Y-%m-%d %H:%M:%S')  # 记录当前时间，使用datatime内置模块
        times_sa = time.mktime(times_sa)
        # 倒计时
        sj = times_sa - time.time()
        if sj < 0:
            sj = ' 开始执行...'
        else:
            sj = '倒计时%.1f秒' % sj
        print("\r 当前 到梦空间脚本 共有 %s个 线程准备完成 目标时间%s %s" % (len(threads), times, sj), end="")
        # 对比时间，时间到的话就执行函数
        if times_sa < time.time():
            starttime = time.time()  # 开始记录时间
            for t in threads:
                t.start()  # 开启线程
            for t in threads:
                t.join()  # 等待所有线程终止
            snatchActivityTime = '%.3f 秒' % (time.time() - starttime)  # 结束时间记录
            log_seva(signUp_values, 1)  # 报名结果储存进日志
            # 没什么卵用的进度条
            print('\n')
            for i in range(1, 101):
                print("\r", end="")
                print("结算中: {}%: ".format(i), "▓" * (i // 2), end="")
                sys.stdout.flush()
                time.sleep(0.025)
            # 结果输入
            print('\n')
            jg = '报名结果如下\n共耗时：%s \n' % (snatchActivityTime)
            print(jg)
            for signUp_s in signUp_values:
                jg += signUp_s[0]
                print(signUp_s[0])
            txt = open('cj/外部插件数据/抢活动结果.txt', 'w', encoding='utf-8')
            txt.write(jg)
            txt.close()
            break
        time.sleep(0.01)
    return '\n脚本执行结束，请输入 "bmjg","/报名结果" 查询'


def dataEliminate():
    for name in os.listdir('cj/到梦空间抢活动/数据'):
        if re.search(r".*txt", name):
            txt = open('cj/到梦空间抢活动/数据/' + name, 'w', encoding='utf-8')
            txt.write('')
            txt.close()
    txt = open('cj/到梦空间抢活动/data.txt', 'w', encoding='utf-8')
    txt.write('')
    txt.close()


# if __name__ == "__main__":
#     buy_times = input("请输入活动报名时间(例如格式：2022-10-28 14:35:00):")  # 时间输入
#     print(main(buy_times, ['杨洪权', '王秀旭', '唐秀厅', '巫鑫']))     # '杨洪权', '王秀旭', '唐秀厅', '巫鑫'

if __name__ == '__main__':
    activeRobberyMain('2022-11-14 18:30:00', ['杨洪权', '唐秀厅', '巫鑫'])
