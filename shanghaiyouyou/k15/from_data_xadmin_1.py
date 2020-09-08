#coding=utf-8
#author:Kingving time:2020/7/19 13:40

from k15.login_xadmin_page import login_xadmin
from requests_toolbelt import MultipartEncoder
import requests
import re


"""文章分类页面"""

s=requests.session()
login_xadmin(s)
url='http://49.235.92.12:8020/xadmin/hello/articleclassify/add/'
r=s.get(url)

csrftoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
# print(csrftoken)

body=MultipartEncoder(
                        fields=[
                        ("csrfmiddlewaretoken",csrftoken[0]),
                        ("csrfmiddlewaretoken", csrftoken[0]),
                        ("n","1323222212"),
                        ("_save","")
    ],)

r3=s.post(url,data=body,headers={'Content-Type': body.content_type})
print(r3.text)



"""新增一篇文章"""


s=requests.session()
login_xadmin(s)
url3='http://49.235.92.12:8020/xadmin/hello/articledetail/add/'
r=s.get(url3)
csrftoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
print(csrftoken)

body3=MultipartEncoder(
                        fields=[
                        ("csrfmiddlewaretoken",csrftoken[0]),
                        ("csrfmiddlewaretoken", csrftoken[0]),
                        ("title","cecece111"),
                        ("auth",'admin111'),
                        ("classify","2"),
                        ("body","输入正文1111111133111"),
                        ("detail","添加备注2222223322222"),
                        ("_save","")
    ],)

r3=s.post(url3,data=body3,headers={'Content-Type': body3.content_type})
print(r3.text)