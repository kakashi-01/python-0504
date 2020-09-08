#coding=utf-8
#author:Kingving time:2020/7/17 22:44

import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree


def login_xadmin(s):
    url='http://49.235.92.12:8020/xadmin/'
    r1=s.get(url) #获取部分cookie，获取页面隐藏参数
    # print(r1.text)
    tokens=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r1.text)
    # print(tokens[0])

    body={
        'csrfmiddlewaretoken':tokens[0],
        'username':'admin',
        'password':'yoyo123456',
        'this_is_the_login_form':'1',
        'next':'/xadmin/'
    }
    r2=s.post(url,data=body)
    # print(r2.text)
    if '主页面 | 后台页面' in r2.text:
        print('登录成功')
    else:
        print('登录失败')

if __name__ == '__main__':
    s=requests.session()
    login_xadmin(s)