#coding=utf-8
#author:Kingving time:2020/6/19 0:28

'''计算 n 的阶乘
计算 n!,例如 n=3(计算 3* 2* 1=6)， 求 10!'''


def foo(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
def main():
    print (foo(10))

if __name__ == '__main__':
    main()
