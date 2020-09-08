#coding=utf-8
#author:Kingving time:2020/7/18 22:08

from k15.login_xadmin_page import login_xadmin
from requests_toolbelt import MultipartEncoder
import requests
import re
from lxml import etree


s = requests.session()
login_xadmin(s)

def add_teacher_name(s):
    #添加老师页面
    url='http://49.235.92.12:8020/xadmin/hello/teacher/add/'

    #获取页面隐藏参数
    r=requests.get(url)
    # print(r.text)

    #使用正则表达式获取token
    csrftoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
    print(csrftoken)

    body=MultipartEncoder(
        fields=[
        ("csrfmiddlewaretoken",csrftoken[0]),
        ("csrfmiddlewaretoken", csrftoken[0]),
        ("teacher_name","yoyo211111114"),
        ("tel","131321313"),
        ("mail","113@qq.com"),
        ("sex","M"),
        ("_save","")
    ],
    )

    r2=s.post(url,data=body,headers={'Content-Type': body.content_type})
    # print(r2.text)
    return r2.text

result=add_teacher_name(s)

#判断是否新增成功
def get_add_result():
    demo=etree.HTML(text)
    nodes=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    print(nodes[0]) #元素对象
    #通过元素对象获取属性
    # print(nodes[0].text)
    get_result=nodes[0].text
    print('获取页面返回结果:%s'%get_result)
    return get_result

if __name__ == '__main__':
    s=requests.session()
    login_xadmin(s)
    text=add_teacher_name(s)
    result=add_teacher_name(text)
    assert result=='yoyo333'

# s=requests.session()
# login_xadmin(s)
# url3='http://49.235.92.12:8020/xadmin/hello/articledetail/add/'
# r=s.get(url3)
# csrftoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
# print(csrftoken)
#
# body3=MultipartEncoder(
#                         fields=[
#                         ("csrfmiddlewaretoken",csrftoken[0]),
#                         ("csrfmiddlewaretoken", csrftoken[0]),
#                         ("title","cecece111"),
#                         ("auth",'admin111'),
#                         ("classify","2"),
#                         ('body','输入正文11111111111'),
#                         ('detail','添加备注22222222222'),
#                         ("_save","")
#     ],)
#
# r3=s.post(url3,data=body3,headers={'Content-Type': body3.content_type})
# print(r3.text)