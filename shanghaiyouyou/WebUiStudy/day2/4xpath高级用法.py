#coding=utf-8
#author:Kingving time:2020/5/27 1:15

'''
xpath使用路径表达式来选取HTML文档中的节点或节点集
'''

from selenium import webdriver

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('D:\QQ\\untitled\\untitled\]untitled\Web自动化测试\day2\\test.html')

# /html/body/div[2]/table/tbody/tr[1]/td--绝对路径-单斜杠（不能跨越选取）
#/html//tr[1]--相对路径（可以跨越选取）-双斜杠，索引定位从1开始

# ancestor 匹配先辈
# ancestor-or-self 匹配先辈和自己



driver.quit()