# coding=utf-8
#author：kingving time:2020/5/18

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#3、找到搜索文本框
input_element=driver.find_element_by_id('kw')

#4、向文本框输入内容
input_element.send_keys('松勤')

#5、找到搜索按钮
search_element=driver.find_element_by_id('su')

#6、点击搜索
search_element.click()
time.sleep(5)

#7、退出
driver.quit()