# 到梦空间活动提醒插件
***
这是一个基于nonebot2的插件，原理与网络抓包相同。

后端使用php可将前后端分离部署(集群自行配置负载均衡)

目前实现了 支持多校、多群发送、参数失效提醒、参数更新、开关功能

### 安装配置

1. 安装nonebot2 [请参阅](https://blog.csdn.net/a1255652/article/details/117613037)
2. 安装定时任务插件 `nb plugin install nonebot-plugin-apscheduler`
3. 安装schedule `pip install schedule`
4. 安装go-cqhttp [请参阅](https://github.com/Mrs4s/go-cqhttp)
5. method.py 中修改后端域名

*问题 1：”No module named 'nonebot.adapters.onebot'“
`pip install nonebot-adapter-onebot`*

### 指令
私聊器人发送 `/帮助` 查看详细指令

## 参数爬取
***
安卓可以使用 HttpCanary

ios可以使用 HTTP Catcher

目标url：```/v2/activity/activities``` 复制响应Body中的d就是参数内容

*注：如果遇到乱码，请检查是否安装了对应的htpps证书*
## 后端
***
### 活动更新检查 - 接口
```
GET /dreamActivityApi
```

#### 请求参数

| 参数名 | 类型   | 必填 | 描述   |
| ------ | ------ | ---- |------|
| schoolId | int | 是   | 学校id |

#### 请求示例

```
GET /dreamActivityApi?schoolId=1001
```

#### 响应参数

| 参数名  | 类型             | 描述           |
| ------- |----------------|--------------|
| error  | boolean        | 请求是否成功       |
| school | string         | 学校名称         |
| admin  | string         | 管理员qq号       |
| qqGroup | array          | 群发群号         |
| msg | array / string | 新活动消息 / 错误信息 |
*注：当error为false时msg为空表示当前时间暂无新活动*

***
### 查询全学校id与管理员qq号反查 - 接口

```
GET /dreamActivityApi/query.php
```

#### 请求参数

| 参数名 | 类型   | 必填  | 描述     |
| ------ | ------ |-----|--------|
| qq | string | 否   | 管理员qq号 |

#### 请求示例

```
GET /dreamActivityApi/query.php?qq=153311...
```

#### 响应参数

| 参数名  | 类型             | 描述   |
| ------- |----------------|------|
| error  | boolean        | 请求是否成功 |
| uuid | array / string | 学校id |

***
### d参数更新与关闭活动更新 - 接口

```
GET /dreamActivityApi/modify.php
```

#### 请求参数

| 参数名 | 类型   | 必填  | 描述      |
| ------ | ------ |-----|---------|
| admin | string | 是   | 管理员qq号  |
| d | string | 否   | 更新的参数   |
| close | string | 否   | 开启、关闭更新 |
*注：close填入任意字符串均可执行，d、close至少填写一个*

#### 请求示例

```
GET /dreamActivityApi/modify.php?admin=153311...&d=ASIssd1...
```

#### 响应参数

| 参数名  | 类型             | 描述     |
| ------- |----------------|--------|
| error  | boolean        | 请求是否成功 |
| msg | string | 执行结果   |

## 服务器持续运行
***
你可以配合 pm2 来守护进程，防止被杀死，详情询问 ChatGPT。

```restart.py``` 可以帮助你每日重启nonebot2、go-cqhttp

```cd /QQ-bot/InceptionQQbot-master/ && nohup nb run &```

```cd /QQ-bot/go-cqhttp/ && nohup go-cqhttp &```

```cd /QQ-bot/ && nohup python restart.py &```