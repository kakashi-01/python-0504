#coding=utf-8
#author:Kingving time:2020/5/25 0:40

from selenium import webdriver
from selenium.webdriver.common.by import By

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('file:///D:/QQ/untitled/untitled/untitled/Web自动化测试/day1/test2.html')

#3、元素定位的另一种方式，为po模式做准备
ele=driver.find_element(By.ID,'abc')
print(ele.text)

#4、获取元素的属性值
print(ele.get_attribute('href')) #定位元素超链接

ele1=driver.find_element(By.CLASS_NAME,'abd')
print(ele1.text)

print(ele1.get_attribute('title'))#定位标题元素

driver.quit()
