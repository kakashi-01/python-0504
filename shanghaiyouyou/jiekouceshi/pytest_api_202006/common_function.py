#coding=utf-8
#author:Kingving time:2020/6/29 23:00

import json
import requests

#登陆
def login(s,username='test',password='123456'):
    """
    登陆函数
    :param s: requests.session()
    :param username:账号
    :param password: 密码
    :return: s
    """

    url='http://49.235.92.12:9000/api/v1/login'

    body={
        "usename":username,
        "password":password
    }

    r=s.post(url,json=body) #先登录

    token=r.json()["token"]
    print(token) #获取到token
    # s.token=token

    h = {
        'Content-Type':'application/json',
        'Authorization': 'Token {token}'.format(token=token)
    }
    s.headers.update(h)
    return s

#修改
def update_info(name='test',mail='2222@qq.com'):
    url='http://49.235.92.12:9000/api/v1/userinfo'
    body={
        'name':name,
        'sex':'M',
        'age':23,
        'mail':mail
    }
    r=s.post(url,json=body)
    return r.json

#查询
def get_info(s):
    url = 'http://49.235.92.12:9000/api/v1/userinfo'
    r=s.post(url)



if __name__ == '__main__':
    s=requests.session()
    login(s)

    infos=update_info(s,name='test',mail='xxx@qq.com')
    print(infos)
    #查询
    m=get_info(s)
    print(m)