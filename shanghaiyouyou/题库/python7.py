#coding=utf-8
#author:Kingving time:2020/7/19 17:47

'''python作业7-如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，* 因为6 = 1+2+3；
下一个完全数是28 = 14+7+4+2+1。 
求1000以下的完全数'''
#方法1
a=range(1,1001)
b=range(1,1001)
result=[]
for i in a:
    tmp=[]
    for k in b:
        if k<i:
            if not i%k:
                tmp.append(k)
            else:
                continue
        else:
            break
    count=0
    for m in tmp:
        count=count+m
    if count==i:
        result.append(i)
    else:
        continue
print (result)


#方法2
a=range(1,1001)
b=range(1,1001)
result=[]
for i in a:
    tmp=[]
    for k in b:
        if k<i:
            if not i%k:
                tmp.append(k)
            else:
                continue
        else:
            break
    count=sum(tmp)
    if count==i:
        result.append(i)
    else:
        continue
print (result)

#方法3
a=range(1,1001)
perfect=[]
for i in a:
    tmp=[]
    for k in range(1,i):
        if not i%k:
            tmp.append(k)
    count=sum(tmp)
    if count==i:
        perfect.append(i)
print (perfect)

#方法4（史上最简单的方式了）
for i in range(1,1000):
    s=0
    for k in range(1,i):
        if i%k==0:
            s=s+k
    if i==s:
        print (i)

