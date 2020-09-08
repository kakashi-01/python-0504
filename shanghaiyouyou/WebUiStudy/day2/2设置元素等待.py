#coding=utf-8
#author:Kingving time:2020/5/26 23:51

from selenium import webdriver

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、设置隐式等待(一次设置全局使用，一直生效）优点是简单，缺点是浪费时间
driver.implicitly_wait(10)

#3、访问网址
driver.get('http://www.baidu.com')

ele=driver.find_element_by_id('kw').send_keys('松勤\n')

driver.find_element_by_link_text('松勤软件测试_松勤软件测试腾讯课堂').click()

driver.quit()
