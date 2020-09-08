#coding=utf-8
#author:Kingving time:2020/5/27 0:51

#显示等待用的比较多，主要使用于.click()那个元素定位

from selenium import webdriver
from selenium.webdriver.common.by import By #设置元素定位方法，用什么方法定位
from selenium.webdriver.support.ui import WebDriverWait #提供等待方法类
from selenium.webdriver.support import expected_conditions as EC #提供判断条件

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、设置隐式等待(一次设置全局使用，一直生效）优点是简单，缺点是浪费时间
driver.implicitly_wait(10)

#3、访问网址
driver.get('http://www.baidu.com') #get会等待元素所有加载完成

driver.find_element_by_id('kw').send_keys('松勤\n')

# driver.find_element_by_link_text('松勤软件测试_松勤软件测试腾讯课堂').click()

# 每隔0.5秒检查一次，最多等待10秒（timeout），会返回元素对象
ele1=WebDriverWait(driver,10,0.5).until(
    EC.visibility_of_element_located(
    (By.LINK_TEXT,'松勤软件测试_松勤软件测试腾讯课堂')
    )
)
ele1.click()

driver.quit()

