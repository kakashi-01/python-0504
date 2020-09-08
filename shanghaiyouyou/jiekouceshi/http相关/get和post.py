#coding=utf-8
#author:Kingving time:2020/6/23 22:16

'''
1
Get肯定没有请求body
Post有请求body（当然请求body也可以为空）

2
安全性上：没有哪个更安全，get会显示在地址栏，而只是post不显示在地址栏，F12中或者fiddler抓包中还是可以看到

get请求==更新 查询
post请求==提交 比如登录账号密码等
put请求==修改
delete请求==删除
增删改查===PDUG

3
请求方法
HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法
HTTP1.1新增了五种请求方法：OPTIONS, PUT（修改数据）, DELETE（删除数据）, TRACE 和 CONNECT 方法

GET 请求指定的页面信息，并返回实体主体
HEAD 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头 POST 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。 PUT 从客户端向服务器传送的数据取代指定的文档的内容。
DELETE 请求服务器删除指定的页面
CONNECT HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器   OPTIONS 允许客户端查看服务器的性能
TRACE 回显服务器收到的请求，主要用于测试或诊断

'''
