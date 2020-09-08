#coding=utf-8
#author:Kingving time:2020/6/29 0:18


import requests

s=requests.Session()#Session的实例

print(s.headers)

#修改头部信息，伪装成浏览器发出的请求
h={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

s.headers.update(h)

print(s.headers) #伪装成浏览器user-agent

print(s.verify) #默认是True，当发起https请求时，不校验证书，改变属性为False

r=s.get('https://www.baidu.com',verify=False) #此时不需要校验证书

r1=s.get('https://www.baidu.com')

print(r1.text)