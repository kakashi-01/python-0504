#coding=utf-8
#author:Kingving time:2020/6/5 23:28

from selenium import webdriver
import win32com.client
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('https://tinypng.com/')

#3、对于input实现的上传功能，通过sendkeys制定本地文件路径即可实现上传
# ele.sendkeys('xxxxx')

#4、先触发文件上传，点击文件上传按钮
driver.find_element_by_css_selector('.target>.icon').click()
time.sleep(3) #打开文件显示需要时间

#5、创建Windows shell对象 （类似cmd）
sh=win32com.client.Dispatch('WScript.shell')
sh.Sendkeys('D:\QQ\\untitled\\untitled\\untitled\Web\day5\\all.png\n') #输入的时候，要切换成英文键盘