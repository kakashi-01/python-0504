#coding=utf-8
#author:Kingving time:2020/6/24 0:15

# 响应状态码：
# 状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别:
# 1xx：指示信息--表示请求已接收，继续处理
# 2xx：成功--表示请求已被成功接收、理解、接受
# 3xx：重定向--要完成请求必须进行更进一步的操作
# 301- 永久重定向
# 302- 临时重定向
# 304- 用到缓存，请求服务端资源未改变，用本地未过期缓存
# 4xx：客户端错误--请求有语法错误或请求无法实现
# 5xx：服务器端错误--服务器未能实现合法的请求
#
# 常见状态码：
# 200 OK //客户端请求成功
# 400 Bad Request //客户端请求有语法错误，不能被服务器所理解
# 401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
# 403 Forbidden  //服务器收到请求，但是拒绝提供服务 (没访问权限)
# 400 bad request：400 Bad Request 是由于明显的客户端错误（例如，格式错误的请求语法，太大的大小，无效的请求消息或欺骗性路由请求），服务器不能或不会处理该请求。
# 404 Not Found //请求资源不存在，eg：输入了错误的URL
# 500 Internal Server Error //服务器发生不可预期的错误
# 503 Server Unavailable //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
