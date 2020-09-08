# -*- coding: utf-8 -*-
# @Author   : 'Kakashi'
# @Date     : 2020-05-18
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/lyz/PycharmProjects/python-0504/day0/ff.html")
# q=driver.find_element_by_xpath('/html/body/div/select/option[2]')
q=driver.find_element_by_link_text('访问百度').click()
print(q.text)
driver.implicitly_wait()