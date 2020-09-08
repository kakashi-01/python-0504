#coding=utf-8
#author:Kingving time:2020/6/23 0:41

#http协议(超文本传输协议）基于请求与响应模式的，无状态的、应用层的协议

#URL：http/https:ip+host,还有一些是域名（需要申请，通过映射原网址）

'''
百度搜索的一个url地址：
https://www.baidu.com/s?wd=%E4%B8%8A%E6%B5%B7%E6%82%A0%E6%82%A0%E5%8D%9A%E5%AE%A2&rsv_spt=1&rsv_iqid=0x91baaabd00070ba2&issp=1&f=8&rsv_bp=1&rsv_idx=2

1.http/https:         协议类型
2.host：主机地址或域名
--192.168.x.xx:8080      地址+端口号
--www.xxx.com            域名
--localhost:8080         localhost是本机地址
3.port:端口号            （默认端口是80可以省略）
4.path:                  请求的路径（host之后，问号？之前）
5.?  :                   问号是分割符号
6.参数：                  name=value
7.&  ：                 多个参数用&隔开
8.编码：urlencode编码

'''