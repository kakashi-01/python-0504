#coding=utf-8
#author:Kingving time:2020/6/5 23:58

from selenium import webdriver

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('https://www.baidu.com')

#3、获得cookie信息
cook=driver.get_cookies()

#4、将获得的cookie信息打印出来
for cookDic in cook:
    print(cookDic)

driver.quit()