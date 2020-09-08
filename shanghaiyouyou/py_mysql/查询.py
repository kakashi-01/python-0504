#coding=utf-8
#author:Kingving time:2020/6/17 0:49

import pymysql

db=pymysql.connect(host='139.159.162.37',
                   port=3306,
                    user='root',
                   passwd='root@123',
                   db='test')

#新建游标
cur=db.cursor()
#写sql语句，查询内容
sql='select * from testt'
#执行sql查询
cur.execute(sql)
#获取查询的返回结果
data=cur.fetchall()
#打印结果
print(data)
#关闭mysql
db.close()

#查询结果数据筛选
firstdata=data[0]
print(firstdata)
print(firstdata[-1])

#查询元祖中的某个值
for i in data:
    if 'xxx' in i:
        print(i[-1])
