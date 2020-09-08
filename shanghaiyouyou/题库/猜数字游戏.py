#coding=utf-8
#author:Kingving time:2020/6/22 0:12

'''随机生成一个整数，如果大于该数提示太大了，如果小于该数提示太小了'''


'''方法1
key = 7
while 1:
    guess = input("请输入一个1-20的整数：")
    guess = int(guess)
    if guess > key:
        print("输入的太大了")
    elif guess < key:
        print("输入的太小了")
    elif guess == key:
     print("恭喜猜对了")
    break
'''

# 方法2
'''
import random #输入随机数
a = 1
b = 99
key = random.randint(1, 100) #随机数范围
while 1:
    guess = int(input("请输入一个整数%d" % a + "到%d:" % b))
    if guess<key and guess > a:
        a = guess
        print('请输入%d到' % a+"到%d:" % b)
    elif guess>key and guess<b:
        b = guess
        print('请输入%d' % a+"到%d:" % b)
    elif guess <= 1 or guess >= 100:
        print("小伙子，别调皮，请重新输入")
    elif guess == key:
        print('真聪明，猜对了！')
        break
'''