#coding=utf-8
#author:Kingving time:2020/6/6 0:20
from selenium import webdriver

cookieSli=[{'domain': '.baidu.com',
            'httpOnly': False,
            'name': 'H_PS_PSSID',
            'path': '/',
            'secure': False,
            'value': '31730_1436_31670_21094_31069_31714_30824_31846_26350_22157'},
{'domain': '.baidu.com',
 # 'expiry': 1622910610,
 'httpOnly': False,
 'name': 'BAIDUID',
 'path': '/',
 'secure': False,
 'value': 'C3B4800B2FAA972F10D2B026DFD6B926:FG=1'},
{'domain': '.baidu.com',
 # 'expiry': 3738858257,
 'httpOnly': False,
 'name': 'BIDUPSID',
 'path': '/',
 'secure': False,
 'value': 'C3B4800B2FAA972F446D53948A55712F'},
{'domain': '.baidu.com',
 # 'expiry': 3738858257,
 'httpOnly': False,
 'name': 'PSTM',
 'path': '/',
 'secure': False,
 'value': '1591374610'},
{'domain': 'www.baidu.com',
 # 'expiry': 1592238610,
 'httpOnly': False,
 'name': 'BD_UPN',
 'path': '/',
 'secure': False,
 'value': '12314753'},
{'domain': 'www.baidu.com',
 'httpOnly': False,
 'name': 'BD_HOME',
 'path': '/',
 'secure': False, 'value': '1'}]


#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('https://www.baidu.com')

#3、清除所有cookie
driver.delete_all_cookies()

for cook in cookieSli:
    #添加cookie
    driver.add_cookie(cook)

driver.refresh()