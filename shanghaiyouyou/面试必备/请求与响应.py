#coding=utf-8
#author:Kingving time:2020/6/24 0:07

"""
1、Request组成:
客户端发送一个HTTP请求到服务器的请求消息包括以下格式：
请求行（request line）、请求头部（header）、空行和请求数据四个部分组成。

2、请求头
Client 客户端
Accept浏览器可接受的媒体类型
Accept-Language: 语言
Accept-Encoding：编码格式
User-Agent：客户端类型
Cookie: 身份认证
Entity:
Content-Type:发送post时候，body的数据类型声明

3、Get请求参数都在请求行里，可以在Webforms的QueryString查看

4、post请求参数可以是请求行的参数QueryString+body
--QueryString可以为空
--body也可以为空
Body参数的数据类型
Content-Type: application/x-www-form-urlencoded


5、Post的body
Post的body常见的数据类型有5种
查看Raw里面的头部Content-Type
1.第一种：application/json： {“key1":"xxx",“key2":“xxxx",“key3":false}
2.第二种：application/x-www-form-urlencoded： key1 =xxx&key2=ooo&key3=false
3.第三种：multipart/form-data:这一种是表单格式的
4.第四种：text/xml
<!--?xml version="1.0"?-->
<methodcall>
<methodname>examples.getStateName</methodname>
5.还有文件下载的时候
Content-Type:  octets/stream



6、Respose结果
一般情况下，服务器接收并处理客户端发过来的请求后会返回一个HTTP的响应消息。
HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文。


状态码（必问）：
状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别:
1xx：指示信息--表示请求已接收，继续处理
2xx：成功--表示请求已被成功接收、理解、接受
3xx：重定向--要完成请求必须进行更进一步的操作
301- 永久重定向
302- 临时重定向
304- 用到缓存，请求服务端资源未改变，用本地未过期缓存
4xx：客户端错误--请求有语法错误或请求无法实现
5xx：服务器端错误--服务器未能实现合法的请求

常见状态码：
200 OK //客户端请求成功
400 Bad Request //客户端请求有语法错误，不能被服务器所理解
401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
403 Forbidden  //服务器收到请求，但是拒绝提供服务 (没访问权限)
400 bad request：400 Bad Request 是由于明显的客户端错误（例如，格式错误的请求语法，太大的大小，无效的请求消息或欺骗性路由请求），服务器不能或不会处理该请求。
404 Not Found //请求资源不存在，eg：输入了错误的URL
500 Internal Server Error //服务器发生不可预期的错误
503 Server Unavailable //服务器当前不能处理客户端的请求，一段时间后可能恢复正常






"""
