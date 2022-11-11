# 初始机器人
1. 安装nonebot2 `pip install nb-cli`
2. 安装定时任务插件 `nb plugin install nonebot-plugin-docs`
3. 安装go-cqgttp `https://github.com/Mrs4s/go-cqhttp/releases`
4. 安装schedule `pip install schedule`
## 如何配置

1. 进入新建文件夹输入 `go-cqhttp` 配置机器人.
2. 修改config.yml.
3. 输入 `go-cqhttp` 启动机器人
4. 解压代码文件并设置相关信息使用 `nb run` 启动.

## 文档

请参阅 [nonebot2 安装与使用](https://blog.csdn.net/a1255652/article/details/117613037)

## 指令
nonebot2 `cd /QQ-bot/InceptionQQbot-master/ ; nb run`

go-cqhttp `cd /QQ-bot/go-cqhttp/ ; go-cqhttp`

定时重启 `cd /QQ-bot/ ; python restart.py`

QQ中私聊或@机器人回复 `/帮助` 查看详细指令

# 插件|到梦空间活动提醒
通过模拟post请求检查活动
请求中headers与data需要抓包获取，修改到 “到梦空间活动提醒.py” 中（主设备用户）
“__init__.py” 中 `@scheduler.scheduled_job('cron', hour=x, minute=xx)` xx是规定了定时执行的时间。`qun = aaaaaaaa` aa...规定了消息提醒的群号。

# 插件|到梦空间抢活动
通过模拟post请求发送报名包
想添加新报名用户需要在目录下的 ”数据“ 文件夹中创建相应名称的txt文件。同时为了保证发送时候不出现堵塞导致报名失败，请在 “config.py” 中增加phoneID类下的headers_Android参数，请保证其数量至少>=报名人数。headers_Apple参数为主设备使用参数。
“Active_robbery.py” 中 65 与 91 行可以设定不需要进行模拟登陆的人员。（一般来说主设备不要重复登陆）
