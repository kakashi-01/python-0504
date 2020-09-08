#coding=utf-8
#author:Kingving time:2020/5/28 23:43
'''
元素定位优先级：ID>NAME>CSS>Xpath
css全称 css selector
项目中元素定位用的最多的是CSS和XPATH，优先级CSS最高
因为CSS是专门用来配合html工作的，它实现的原理是匹配对象的原理；而XPATH是配合XML工作的，实现的原理是遍历文档
CSS性能更加优秀，相对于XPATH来说CSS的语法更加简洁明了
前端开发主要用的是CSS，不适用XPATH
'''
from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

