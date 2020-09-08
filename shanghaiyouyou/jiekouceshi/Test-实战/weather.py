#coding=utf-8
#author:Kingving time:2020/6/24 23:44


import  requests

# url='http://api.juheapi.com/japi/toh'
# querystring='57d46b7258fc47e14290c33537f23d36'
#
# r=requests.get(url,params=querystring)
#
# print(r.text)

# url='http://web.juhe.cn:8080/constellation/getAll'
# querystring='cde5e16435cd0217f505a88898b60707'
#
# r=requests.get(url,params=querystring,verify=False)
#
# print(r.text)


url = 'http://japi.juhe.cn/qqevaluate/qq'
par = {'key': '8dbee1fcd8627fb6699bce7b986adc45',
'qq' :'283340479'
       }
r =requests.get(url, params=par)
print(r.text)  # 打印返回结果 文本--str
print(r.json()) #打印json格式--dict
print(r.status_code) #打印状态码
print(r.content)#字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
print(r.headers)#以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print(r.url) # 获取url
print(r.encoding)# 编码格式
print(r.cookies) # 获取返回的cookie
#verify=False  忽略对证书的校验（ssl),一般是https的时候会遇见