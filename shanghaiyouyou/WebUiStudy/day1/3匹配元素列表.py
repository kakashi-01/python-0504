#coding=utf-8
#author:Kingving time:2020/5/25 0:29

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('file:///D:/QQ/untitled/untitled/untitled/Web自动化测试/day1/test2.html')

#3、匹配元素列表，返回所有匹配到的元素列表，如果一个也匹配不到，就返回空列表
#   id属性是唯一的
eleSli=driver.find_elements_by_tag_name('p') #elements可以遍历
# for ele in eleSli:
#     print(ele.text)

driver.quit()