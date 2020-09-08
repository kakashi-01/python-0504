#coding=utf-8
#author:Kingving time:2020/5/28 23:04

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#常用方法1：点击、输入操作
'''
driver.find_element_by_id('kw').send_keys('selenium')#针对input标签模拟键盘输入
driver.find_element_by_id('su').click()#点击元素
time.sleep(2)
driver.find_element_by_id('kw').clear()#清空文本
time.sleep(5)
'''

#常用方法2：size 返回元素的尺寸
eleSize=driver.find_element_by_id('kw').size #元素的尺寸
print(eleSize)

#常用方法3：text 获取元素的文本
eleText=driver.find_element_by_xpath('//div[@class=\"title-text c-font-medium c-color-t\"]').text
print(eleText)

#常用方法4：get_attribute 获得属性值
ele=driver.find_element_by_id('virus-2020')
ele.get_attribute('target')
print(ele.get_attribute('target'))
driver.quit()

#常用方法5：is_dispalyed 检测元素是否可见
ele=driver.find_element_by_id('s_is_result_css')
print(ele.is_displayed())

driver.quit()