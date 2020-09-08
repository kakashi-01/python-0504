#coding=utf-8
#author:Kingving time:2020/7/8 23:42

#打印99乘法口诀表

# for i in range(1,10):
#     for a in range(1,10):
#         print('%s*%s=%s'%(i,a,i*a),end='')



#老师的方法
for i in range(1,10):
    for j in range(1,i+1):
        #print 加end参数，不换行
        print('%s*%s=%-2s' %(j,i,i*j),end='  ')
    print() #print空=实现换行功能