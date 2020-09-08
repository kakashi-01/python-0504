#coding=utf-8
#author:Kingving time:2020/5/24 10:19

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://localhost:63342/selenium/day4/test2.html?_ijt=uljgqkjnpbcb9bubmtgg9s8qct')

#第一部曲：定位到需要切换进去的iframe
iframeEle=driver.find_element_by_css_selector('iframe')

#第二部曲：切换进入刚才找到的元素
driver.switch_to.frame(iframeEle)

#第三部曲：开始你的表演
driver.find_element_by_id('kw').send_keys('123\n')

#切换回原来的主页面，也就是最外层
driver.switch_to.default_content()
driver.find_element_by_id('abc').send_keys('这是外层的input')