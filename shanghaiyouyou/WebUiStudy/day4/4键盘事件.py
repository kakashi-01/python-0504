#coding=utf-8
#author:Kingving time:2020/5/24 9:51

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#3、定位到输入框
inpEle=driver.find_element_by_id('kw')
inpEle.send_keys('selenium')
time.sleep(2)

#4、删除最后一个字母
inpEle.send_keys(Keys.BACK_SPACE)

#5、输入空格
inpEle.send_keys(Keys.SPACE)
inpEle.send_keys('安装')

#6、Ctrl+a 全选输入框内容
inpEle.send_keys(Keys.CONTROL,'a')

#7、Ctrl+x 剪切输入框内容
inpEle.send_keys(Keys.CONTROL,'x')
time.sleep(2)
#8、Ctrl+v 粘贴输入框内容
inpEle.send_keys(Keys.CONTROL,'v')
time.sleep(2)

#Keys.SPACE 空格键
#Keys.ENTER 回车键
#Keys.ESCAPE esc按键

driver.quit()