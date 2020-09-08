#coding=utf-8
#author:Kingving time:2020/6/11 20:35

from selenium import webdriver
import pprint

driver=webdriver.Chrome('D:\selenium\chromedriver.exe')
driver.get('http://127.0.0.1:8088/login')
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
driver.find_element_by_css_selector('.login-wrap>button').click()
cookie=driver.get_cookies()
pprint.pprint(cookie)
driver.quit()