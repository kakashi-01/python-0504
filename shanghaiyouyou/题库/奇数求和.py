#coding=utf-8
#author:Kingving time:2020/6/21 23:19


s=0
for i in range(100):
    if i%2: #取奇数
        s+=i
        if s>100: #当S大于100的时候 就不继续循环了
            s=s-i #不要100以后的数据就减去上一个数据
            break #跳出所有循环
    else:
        continue #跳出此次循环，继续下一次循环
print(s)

