#coding=utf-8
#author:Kingving time:2020/5/24 10:49

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

driver.get('http://news.baidu.com')

#浏览器后退操作
driver.back()
time.sleep(2)

#浏览器前进操作
driver.forward()
time.sleep(2)

#浏览器刷新界面
driver.refresh()
time.sleep(2)


'''控制浏览器大小

#3、设置浏览器 宽600 高600显示 （参数像素点设置）
print('设置浏览器宽600，高600')
driver.set_window_size(600,600)
time.sleep(2)

#4、设置浏览器为全屏显示（最大化）
driver.maximize_window()
time.sleep(2)

#5、设置浏览器最小化
driver.minimize_window()
time.sleep(2)
'''




driver.quit()