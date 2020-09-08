#coding=utf-8
#author:Kingving time:2020/5/26 23:33

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#用于获取当前页面的标题
print(driver.title)

#用户获得当前页面的URL
print(driver.current_url)

#获取标签对之间的文本信息
ele=driver.find_element_by_id('kw')
print(ele.text)

ele1=driver.find_element_by_class_name('title-text')
print(ele1.text)

driver.quit()