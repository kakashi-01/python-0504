#coding=utf-8
#author:Kingving time:2020/6/24 0:24

'''
1. Fiddler工作原理
终端设备（web、app）发出请求，fiddler作为代理，传给服务器；服务器返回数据，fiddler拦截后，再传给终端设备。

2. 自定义会话框
自定义会话框，查看get和post请求
1.鼠标放#后面
2.选择Miscellaneous
3.选择RequestMethod

3. 抓https请求
火狐浏览器https请求需要导入证书
（其它浏览器不用导入，如chrome）

4. 手机wifi设置代理
1.手机设置-wifi-找到当前连接的网络（要跟电脑是同一局域网）
2.Fiddler设置允许远程设备连接
3.Cmd输入ipconfig查看ipv4地址

5. 抓app上https请求
1.https的请求需要安装证书（http的话不用安装）
2.手机浏览器输入http://192.168.1.100:8888/
3.要是打不开这个地址，现在电脑上浏览器输入这个地址
（确保fiddler是开着的）
注意：安装证书后，要是fiddler关闭了，是不能正常上网的
（需删去掉wifi代理设置）

6. 设置过滤设备
...from all processes :抓所有的请求
...from browsers only ：只抓浏览器的请求
...from non-browsers only :只抓非浏览器的请求
...from remote clients only:只抓远程客户端（手机app）请求



7.会话保存有什么作用
1.当你测出接口的BUG时候，保留证据给开发（也许开发跟你不是一个公司，远程协助工作这种）
2.后面学写python发接口请求，遇到报错时候，别截图，直接抓会话保存了，发给校长解决
（最讨厌只截个报错，还扣扣巴巴的截一点）
3.遇到问题正确提问姿势：
-- fiddler抓包看request和response 的Raw
-- 代码报错截全
-- 贴代码（别用中文描述，越描述越不清楚）

8.请求断点
修改请求参数，请求断点可以修改请求参数，绕过前端请求
返回断点
修改返回数据，一般用于开发调试某个接口，服务端还没开发好接口，前端需要用到接口返回数据
--- mock (模拟返回数据)
'''