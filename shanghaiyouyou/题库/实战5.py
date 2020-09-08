#coding=utf-8
#author:Kingving time:2020/7/27 1:01

'''把数组[0,1,1,0,1,1,0,1,1,1,0,0]中所有的1排到左侧，0排到有右侧；'''

a=[0,1,1,0,1,1,0,1,1,1,0,0]
s=range(len(a))[::-1]
for i in s:
    for j in range(i):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

lst = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
result_lst = []
for value in lst:
    if value == 1:
        result_lst.append(value)

for value in lst:
    if value == 0:
        result_lst.append(value)

print("处理后的数组为: ", result_lst)

result_lst = []
for value in lst:
    if value == 1:
        result_lst.insert(0, value)
    else:
        result_lst.append(value)

print("处理后的数组为: ", result_lst)

for i in range(len(lst)):
    if lst[i] == 1:
        lst.insert(0,lst.pop(i))

print("处理后的数组为: ",lst)