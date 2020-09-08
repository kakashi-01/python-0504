#coding=utf-8
#author:Kingving time:2020/7/10 1:07

import requests

url='https://www.juhe.cn/docs/api/id/63'

h={'Appkey':'57d46b7258fc47e14290c33537f23d36'}

r=requests.post(url,data=h)

# print(r.text)
print(r.json)