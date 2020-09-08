# coding=utf-8
#author：kingving time:2020/5/18

from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('file:///C:/Users/dell/AppData/Local/Temp/Rar$DRa15472.1174/day4/test.html')


#3、触发对话框
driver.find_element_by_id('bu1').click()
#4、获取对话框
al=driver.switch_to.alert
#5、确认对话框
al.accept() #点击确认
time.sleep(3)


#3、触发确认框
driver.find_element_by_id('bu2').click()
#4、获取确认框
al =driver.switch_to.alert
al.accept() #点击确认
#5、再次触发确认框
driver.find_element_by_id('bu2').click()
al.dismiss()#点击取消


#3、触发提示框
driver.find_element_by_id('bu3').click()
#4、获取提示框
al =driver.switch_to.alert
#5、向提示框中输入内容
al.send_keys('哈哈')
time.sleep(5)
al.accept()#点击确认

time.sleep(5)
driver.quit()

