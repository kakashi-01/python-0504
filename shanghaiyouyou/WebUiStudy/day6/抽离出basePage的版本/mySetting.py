#coding=utf-8
#author:Kingving time:2020/6/7 23:45

from selenium import webdriver

#域名，将网址配置成配置文件
DOMAIN='http://127.0.0.1:8088/login'


#超时时间
TIMEOUT=10

#轮询时间
POLL_FREQUENCY=0.5

#driver路径
driverPath={
    "Chrome":'D:\selenium\chromedriver.exe'
    # 'Firefox''D:\selenium\geodriver.exe'
}

