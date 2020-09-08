#coding=utf-8
#author:Kingving time:2020/5/24 9:32

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.baidu.com')

#3、定位到要悬停的元素
ele=driver.find_element_by_id('s-usersetting-top')

#4、对定位到的元素 进行鼠标悬停操作
ActionChains(driver).move_to_element(ele).perform()

driver.get('file:///C:/Users/dell/AppData/Local/Temp/Rar$DRa15440.7211/day4/test1.html')
#定位到起始元素
startEle=driver.find_element_by_id('blackSquare')
#定位到目标元素
targetEle=driver.find_element_by_id('targetEle')
#元素拖拽，将起始元素，拖拽到目标元素
ActionChains(driver).drag_and_drop(startEle,targetEle).perform()

# ele=driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).context_click(ele).perform() #右击
ActionChains(driver).double_click(ele).perform() #双击
ActionChains(driver).click(ele).perform() #单击