#coding=utf-8
#author:Kingving time:2020/7/8 23:41

# 1、如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。  
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 那么问题来了，求1000以内的水仙花数（3位数）



# 列出水仙花数
for num in range(100, 1000):
    ge_num = num % 10
    bai_num = num // 100
    shi_num = (num - bai_num * 100 - ge_num) // 10
    if ge_num ** 3 + shi_num ** 3 + bai_num ** 3 == num:
        print (num)


# 判断水仙花数
num = int(input('请输入一个三位数'))
ge_num = num % 10
bai_num = num // 100
shi_num = (num - bai_num * 100 - ge_num) // 10
if ge_num ** 3 + shi_num ** 3 + bai_num ** 3 == num:
    print ('%d是水仙花数' % num)

else:
    print ('%d不是水仙花数' % num)

