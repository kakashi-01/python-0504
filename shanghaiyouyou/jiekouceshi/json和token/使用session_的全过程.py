#coding=utf-8
#author:Kingving time:2020/6/29 0:54

import requests
import re #正则提取

url='http://49.235.92.12:9000/admin/login/'

s=requests.Session()

#模拟第一次打开登录页面
r1=s.get(url)
print(r1.text)

#获取页面隐藏参数csrf_token
csrf_token=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r1.text)
print(csrf_token[0])

#cookie读取
print(s.cookies) #RequestsCookieJar
print(dict(s.cookies))

#后面的登录
body={
    "csrfmiddlewaretoken": csrf_token[0],
    "username": "admin",
    "password": "yoyo123456",
    "next": "/admin/"
}

r2=s.post(url,data=body)
#print(r2.text)

assert 'site adminstration | Django site admin' in r2.text

print(s.cookies)


#登录之后的页面
r3=s.get('http://49.235.92.12:9000/admin/auth/group/')
print(r3.text)