# -*- coding: utf-8 -*-
# @Author   : 'Kakashi'
# @Date     : 2020-05-15
import time
from selenium import webdriver
driver=webdriver.Chrome(r'C:\fengjianwei\Autotest_Study\autotest_ready\3.selenium_ready\chromedriver.exe')
driver.get('https://www.baidu.com/')
ele=driver.find_element_by_id('kw')
ele.send_keys('chromdriver')
btn=driver.find_element_by_id('su')
btn.click()
time.sleep(2)

res=driver.find_element_by_id('1')
if 'chromedriver minor'in res.text:
    print('pass')
else:
    print('fail')
    print(res.text)
driver.quit()