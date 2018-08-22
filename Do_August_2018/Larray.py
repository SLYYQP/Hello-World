#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# create array
a1 = np.array((1, 2, 3, 4, 5))# 参数是元组
a2 = np.array([6, 7, 8, 9, 0])# 参数是list
a3 = np.array([[1, 2, 3], [4, 5, 6]])# 参数二维list
print(a1, a2, a3)
print(a3.shape)#得到c的形状是2行3列

a4 = np.array([[1, 2], [3, 4], [5, 6]])#创建3行2列二维数组。

a5 = np.zeros(6)#创建长度为6的，元素都是0一维数组
a6 = np.zeros((2,3))#创建3行2列，元素都是0的二维数组
a7 = np.ones((2,3))#创建3行2列，元素都是1的二维数组
a8 = np.empty((2,3)) #创建3行2列,未初始化的二维数组
a9 = np.arange(6)#创建长度为6的，一维数组array([0, 1, 2, 3, 4, 5])
a10 = np.arange(1,7,2)#结果与np.arange(6)一样。第一，二个参数意思是数值从1〜6,不包括7.第三个参数表步长为2
a11 = np.linspace(0,10,7) # 生成首位是0，末位是10，含7个数的等差数列
a12 = np.logspace(0,4,5)#用于生成首位是10**0，末位是10**4，含5个数的等比数列
print(a8, a9, a10, a11)
print("..........................................分割线...................................................")
# add
b1 = np.array([[1, 2], [3, 4], [5, 6]])
b2 = np.array([[10, 20], [30, 40], [50, 60]])

b3 = np.append(b1, 7)
b4 = np.append(b1, b2)
print(b3)
print(b4)
b5 = np.vstack((b1, b2))
b6 = np.hstack((b1, b2))
print(b5)
print(b6)
print("..........................................分割线...................................................")
# search
c1 = np.array([[1, 2], [3, 4], [5, 6]])
print(c1[0])# array([1, 2])
print(c1[0][1])#2
print(c1[0, 1])#2
c2 = np.arange(6)#array([0, 1, 2, 3, 4, 5])
print(c2[1:3])#右边开区间,array([1, 2])
print(c2[:3])#左边默认为0,array([0, 1, 2])
print(c2[3:])#右边默认为元素个数,array([3, 4, 5])
print(c2[0:4:2])#下标递增2,array([0, 2])
"""
1. np.where(condition, x, y)
满足条件(condition)，输出x，不满足输出y。
如果是一维数组，相当于[xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
2. np.where(condition)
只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)。
这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。
"""
#NumPy的where函数使用
#np.where(condition, x, y)，第一个参数为一个布尔数组，第二个参数和第三个参数可以是标量也可以是数组。
cond1 = np.array([True, False, True, False])
print("cond1:", cond1)
c3 = np.where(cond1, -2, 2)# [-2  2 -2  2]
print("c3:", c3)
cond2 = np.array([1, 2, 3, 4])
print("cond2:", cond2)
c4 = np.where(cond2 > 2, -2, 2)# [ 2  2 -2 -2]
print("c4:", c4)
c5 = np.array([-1, -2, -3, -4])
print("c5:", c5)
c6 = np.array([1, 2, 3, 4])
print("c6:", c6)
c7 = np.where(cond2 > 2, c5, c6) # 长度须匹配[1,2,-3,-4]
print("c7:", c7)
c8 = np.where(cond2 > 2)
print("c8:", c8)
print("..........................................分割线...................................................")
# modify
d1 = np.array([[1, 2], [3, 4], [5, 6]])
d1[0] = [11, 22]  # 修改第一行数组[1,2]为[11,22]。
d1[0][0] = 111  # 修改第一个元素为111,修改后,第一个元素“1”改为“111”。
print("d1:", d1)
d2 = np.array([[1, 2], [3, 4], [5, 6]])
d3 = np.array([[10, 20], [30, 40], [50, 60]])
d2 + d3 # 加法必须在两个相同大小的数组键间运算,对应元素相加。
print("d2 + d3 :", d2 + d3)
#不同维数的数组直接相加显然是不允许的。但是可以用一个n行列向量和一个m列行向量构造出一个n×m矩阵
d4 = np.array([[1], [2]])
print("d4:", d4)
list1 = ([[10, 20, 30]])  # 生成一个list，注意，不是np.array。
print("list1:", list1)
print("d4 + list1:", d4 + list1)
d5 = np.array([10, 20, 30])
print("d5:", d5)
print("d5.shape：", d5.shape)
print("d4 + d5", d4 + d5)
#数组和一个数字的加减乘除的运算，相当于一个广播，把这个运算广播到各个元素中去.
d6 = np.array([[1, 2], [3, 4], [5, 6]])
print("d6*2:", d6*2)#相当于a中各个元素都乘以2.类似于广播。
print("d6**2:", d6**2)#每个元素的2次方
print("d6 > 3:", d6 > 3)
print("d6 + 3:", d6 + 3)
print("d6 / 2:", d6 / 2)

print("..........................................分割线...................................................")
# delete
#方法一：
#利用查找中的方法，比如a=a[0]，操作完居后，a的行数只剩一行了。
e1 = np.array([[1, 2], [3, 4], [5, 6]])#array([1, 2])
print("e1[0]:", e1[0])
#方法二：
e2 = np.array([[1, 2], [3, 4], [5, 6]])
print("删除俄e2的第二行：", np.delete(e2, 1, axis=0))#删除e2的第二行。
print("删除e2的第二、三行:", np.delete(e2, (1, 2), 0))#删除e2的第二，三行。
print("删除e2的第二列:", np.delete(e2, 1, axis=1))#删除e2的第二列。
#方法三：
#先分割，再按切片a=a[0]赋值。
e3 = np.array([[1, 2], [3, 4], [5, 6]])
print("水平分割：", np.hsplit(e3, 2)) # 水平分割（搞不懂，明明是垂直分割嘛？）
print("与np.hsplit(a,2)效果一样:", np.split(e3, 2, axis=1))  # 与np.hsplit(a,2)效果一样。
print(np.vsplit(e3, 3))
print("与np.vsplit(a,3)效果一样:", np.split(e3, 3, axis=0))  # 与np.vsplit(a,3)效果一样。
print("..........................................分割线...................................................")
# traversal
f1 = np.arange(9).reshape(3, 3)
print("f1:", f1)
for row in f1:
    print("row:", row)
'''
[0 1 2]
[3 4 5]
[6 7 8]
'''
# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
for element in f1.flat:
    print("element", element)
'''
0 1 2 3 4 5 6 7 8
'''
[rows, cols] = f1.shape
for i in range(rows-1):
    for j in range(cols-1):
        print("f1[j, i]:", f1[j, i])

