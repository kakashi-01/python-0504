#coding=utf-8
#author:Kingving time:2020/6/5 23:20

from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('D:\QQ\\untitled\\untitled\\untitled\Web自动化测试\day5\\test.html')


#3、定位到下拉框元素
ele=driver.find_element_by_id('abc')

#4、根据下拉框文本选择
# Select(ele).select_by_visible_text('月薪三万')#根据文本选择

#5、根据value属性选择
# Select(ele).select_by_value('p3')

#6、根据下标选择
# Select(ele).select_by_index('2')