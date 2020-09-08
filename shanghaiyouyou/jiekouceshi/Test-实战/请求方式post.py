#coding=utf-8
#author:Kingving time:2020/6/25 0:36

#1、ssl证书
# https的请求相对于http安全级别高，需要验证SSL证书
import urllib3  # 使用这个方法就OK了
# urllib3.disable_warnings()  # 忽略警告

#2、报SSL问题，主要是fiddler开着导致的，解决办法：关掉就行

# 调试时候，可以加个参数 verify=False

#3、post请求参数

'''
Post请求参数一部分在url里，另外一部分在body里面

1.第一种：application/json： {“key1“:”value1”,“keyt2":“value2"}
json=
 
2.第二种：application/x-www-form-urlencoded：name1= value1&name2=value2
data=
 
3.第三种：multipart/form-data:这一种是表单格式的
（文件上传 file=，图片上传等混合式）
data=

4. Content-Type:octets/stream
（文件下载） 
data=

5.text/xml
data=
'''

#4、不带body的post请求
# Post请求的body是可以没有的，比如下面这个post接口，参数都在url上，这种post请求就不需要传body
import requests
url = "http://v.juhe.cn/weather/index"
par = {"cityname": "上海",  # 城市名或城市ID，如："苏州"，需要utf8 urlencode
 "dtype": "json", # 返回数据格式：json或xml,默认json
"format": "1",# 未来7天预报(future)两种返回格式，1或2，默认1
 "key": "80b4d4e1d870d257d3344fcf2d08f64a"}
r1 = requests.post(url, params=par)
print(r1.text)


# -----------------------------------------------------------------------------------------------------
#1. Body为json
# application/json 直接传json=body
host = "http://49.235.92.12:9000"
login_path = "/api/v1/login/"
body = {
    "username": "test",
    "password": "123456"
                        }
# application/json 直接传json=body
r = requests.post(url=host+login_path, json=body)
print(r.text)

#2. Body为x-www-form-urlencoded---data=body
data=body



#正则表达式---获取token,token动态变化的，所以用正则表达式来获取，做为动态关联
import re
csrf_token=re.findall("'csr'value='(.+?)",r1.text)
print(csrf_token[0])


#断点
assert xxxx in r1.text

#或者用if语句判断
if xxx in r1.text:
    print('登录成功')
else:
    print('登录失败')


#session
s=requests.sessions()
r1=s.post(url,data=body)
# 通过session发请求，来关联