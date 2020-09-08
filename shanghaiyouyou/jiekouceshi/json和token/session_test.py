#coding=utf-8
#author:Kingving time:2020/6/29 0:31

#Session保持会话，跨请求保存token

import requests
import json

s=requests.session()

url='http://49.235.92.12:6009/api/v1/login'

body={
    "usename":"test",
    "password":"123456"
}

r=s.post(url,json=body) #先登录

token=r.json()["token"]
print(token) #获取到token

#保存token到session会话
s.token=token

print(s.token)
#传头部，获取自动更新的token
h={
'Authorization': 'Token {token}'.format(token=token)
}
s.headers.update(h) #更新头部

print(s.headers)

#后面请求不需要传token
r2=s.get('http://49.235.92.12:6009/api/v1/userinfo')



# -----------------------
#修改个人信息
url2='http://49.235.92.12:6009/api/v1/userinfo'

body2={
"name": "test",
"sex": "M",
"age": 20,
"mail": "283340479@qq.com"
}
r3=s.post(url2,json=body2)

print(r3.text)