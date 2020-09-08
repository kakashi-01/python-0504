#coding=utf-8
#author:Kingving time:2020/6/17 1:13

import pymysql

db=pymysql.connect(host='139.159.162.37',
                   port=3306,
                    user='root',
                   passwd='root@123',
                   db='test')

#新建游标
cur=db.cursor()
#写sql语句，更新内容
sql_update="""
update shangpin
set sp_status=2,sp_status_name='支付失败'
where ip=1001
"""
#执行sql更新
cur.execute(sql_update)
#需要用commit提交数据
db.commit()
#无返回结果，去数据看是否已经少了一条对应数据

#关闭mysql
db.close()