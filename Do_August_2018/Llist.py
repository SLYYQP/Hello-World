#!/usr/bin/python
# -*- coding: UTF-8 -*-



# create
# list是python基本数据类型 python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。
print("..........................................Create...................................................")
c1 = ['Google', 'Runoob', 1997, 2000]
c2 = [1, 2, 3, 4, 5]
c3 = ["a", "b", "c", "d"]

print("c1:", c1, "\n", "c2:", c2, "\n", "c3:", c3, "\n")

c4 = [x for x in range(10)]
print("c4:", c4)

# add
print("..........................................Add...................................................")
a1 = []          # 空列表
#append
a1.append('Google')   #使用 append() 添加元素
a1.append('Runoob')
print("a1:", a1)

#extend
#有关于用extend拓展列表的方法，要注意的是，此方法是用列表去拓展列表，而不是直接添加元素，所以“（）”中要加上“[]”。
a1.extend(["extend1", "extend2"])
print("after extend:", a1)

#insert
a1.insert(1, "insert2")
print("after insert:", a1)

# search
#使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
print("..........................................Search...................................................")
s1 = ['Google', 'Runoob', 1997, 2000]
s2 = [0, 1, 2, 3, 4, 5, 6, 7]

print("s1[0]: ", s1[0])
print("s2[1:5]: ", s2[1:5])
print("查找索引：", s1.index("Google"))
print("倒序访问：", s1[-1])
print("从头开始取：", s2[:3])
print("取到末尾：", s2[3:])
print("全取：", s2[:])
print("步长 2：", s2[:6:2])
print("步长 3：", s2[::3])
print("步长为负数从右往左取：", s2[::-1])

# modify
print("..........................................Modify...................................................")
m1 = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", m1[2])
m1[2] = 2001
print("更新后的第三个元素为 : ", m1[2])

m1[m1.index("Google")] = "Baidu"
print("根据索引重新赋值：", m1)

# delete
print("..........................................Delete...................................................")
d1 = ['Google', 'Baidu', 'Firefox', 2008, 'Runoob', 1997, 2000]

print("原始列表 : ", d1)
del d1[2] #根据索引删除
print("删除第三个元素 : ", d1)

d1.remove("Runoob")
print("remove:", d1) #根据名字删除,如果有重复的值只会删除一个

d1.pop()#默认删除最后一个
print("pop: ", d1)

d1.pop(1) #删除指定位置，如果下标不存在，则报错
print("pop(1):", d1)

d2 = [x for x in range(10)]
d2.clear()#清空整个list
print("before clear：", d2)
print("after clear:", d2)

# Reverse
print("..........................................Reverse...................................................")
r1 = ['Google', 'Baidu', 'Firefox', 2008, 'Runoob', 1997, 2000]
r1.reverse()#反转r1中的元素
print("r1:", r1)

# Sort
print("..........................................Sort...................................................")
num = [9, 12, 0, 45, 78, 35, 999, 567]
num.sort()#排序，默认是升序
print("升序：", num)
num.sort(reverse=True)#降序
print("降序：", num)

def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

random.sort(key=takeSecond, reverse=True)

print("排序列表：", random)

# traversal
print("..........................................Traversal...................................................")
# 1
t1 = ['Google', 'Baidu', 'Firefox', 2008, 'Runoob', 1997, 2000]
print("方法一：")
for t1_id in t1:
    print(t1_id)

# 2
print("方法二：")
for index, t1_id in enumerate(t1):
    print(index, t1_id)

# 3
print("方法三：")
for i in range(len(t1)):
    print(i, t1[i])

# 4
print("方法四：")
for t1_id in iter(t1):
    print(t1_id)

# operations
print("..........................................Operations...................................................")
# 降维 python2
# from compiler.ast import flatten
# list1 = [['1', '5'], ['2', '59', '36'], ['3', '46', '721', '3'], ['4', '5']]
# print flatten(list1)

"""
将二维列表降为一维py3
"""
# 方法一
list1 = [[4, 2, 3], [5, 9, 1], [7, 8, 9]]
from itertools import chain
list11 = list(chain.from_iterable(list1))
print("list11:", list11)

# 方法二
list22 = [','.join(map(str, t)) for t in list1]
print("list22:", list22)

# 方法三
from itertools import starmap
list33 = list(starmap('{},{},{}'.format, list1))
print("list33:", list33)

# 方法四
i = 0
while i < 3:
    list1[i] = str(list1[i])[1:3*3-1]
    i = i + 1
print("list1[0:3]:", list1[0:3])

# 分割
list2 = [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(list2), 2):
    print(list2[i:i+2])

# 分割后放进一个列表中
list3 = [list2[i:i+2] for i in range(0, len(list2), 2)]
print(list3)

"""
列表去重的6种方法
"""
# 方法一,可以保持之前的排列顺序
l1 = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
new_l1 = []
for id in l1:
    if id not in new_l1:
        new_l1.append(id)
print(new_l1)

# 方法二,不会保留之前的顺序
l2 = list(set(l1))
print("l2:", l2)

# 方法三,利用lambda匿名函数和reduce函数处理
"""
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）
先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
reduce() 函数语法：reduce(function, iterable[, initializer])
"""
from functools import reduce
func = lambda x, y: x if y in x else x + [y]
l3 = reduce(func, [[], ] + l1)
print("l3:", l3)

# 方法四,使用itertools模块
import itertools
l1.sort()
it = itertools.groupby(l1)
for k, g in it:
    print("k:", k, list(g))

# 方法五,无法保持原有顺序
l4 = set(l1)
print("l4:", l4)

# 方法六,while遍历去重
l5 = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]

for x in l5:
    while l5.count(x) > 1:   # count统计某个元素在列表种出现的次数
        del l5[l5.index(x)]   # index从列表中找出某个值第一个匹配项的索引位置
print("l5：", l5)

l5 = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
def delReapt(l5):
    for x in l5:
        while l5.count(x) > 1:
            del l5[l5.index(x)]
    return l5

L = delReapt(l5)    # 注意：定义了函数，要使用函数
print("L:", L)
"""
将一维列表中的字符串转换成正型py3
"""
l6 = ['1', '2', '3', '4', '5', '6']
l7 = list(map(int, l6))
print('l7:', l7)

"""
将二维列表中的字符串转换成正型py3
"""
l8 = [['1', '2'], ['3', '4', '5'], ['6', '7', '8', '9']]
list_to_int = []
for each in l8:
    line = list(map(lambda x: int(x), each))
    list_to_int.append(line)
print("list_to_int:", list_to_int)

"""
py2一维列表中的字符串转换成正型
l6 = ['1', '2', '3', '4', '5', '6']
list = map(int, l6)

py2二维列表中的字符串转换成正型
l8 = [['1', '2'], ['3', '4', '5'], ['6', '7', '8', '9']]
list_to_int = map(lambda x: int(x), l8)
"""

"""
打乱列表顺序
"""
import random as rd
lis = [1, 2, 5, 7, 9, 10]
rd.shuffle(lis)
print(lis)