#coding=utf-8
#author:Kingving time:2020/7/13 22:30

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



class UesrInfo():
    '''个人信息'''

    def __init__(self,s:requests.Session):
        self.s=s

    #修改
    def update_info(self,name='test',mail='2222@qq.com'):
        url='http://49.235.92.12:9000/api/v1/userinfo'
        body={
            'name':name,
            'sex':'M',
            'age':23,
            'mail':mail
        }

        r=self.s.post(url,json=body)
        return r.json

    def get_info(self):
        url = 'http://49.235.92.12:9000/api/v1/userinfo'
        r=self.s.get(url)
        return r.json()

if __name__ == '__main__':
    s=requests.session()
    #先登录
    login(s) #函数

    #实例化
    info=UesrInfo(s)
    info.update_info()
    Infos=info.get_info()
    print(Infos)