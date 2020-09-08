# coding=utf-8
#author：kingving time:2020/5/18

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#3、截屏，截屏整个页面
driver.get_screenshot_as_file('./all.png')

#4、截屏，截取特定的某个元素
ele=driver.find_element_by_id('kw')
ele.screenshot('./ele.png')