#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

"""
1、创建一个对象、调用对象方法
"""
# class MyClass:
#     i = 123456
#     def f(self):
#         return "hello world"
#
# # 实例化
# x = MyClass()
#
# print("调用对象方法：", x.f())

"""
2、创建一个数组、列表、字典，它们的元素是对象，对数组和列表中的元素进行排序

    sort 与 sorted 区别：
    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，
    而不是在原来的基础上进行的操作。
    
    语法：sorted(iterable, key=None, reverse=False)  

    参数说明：
    iterable -- 可迭代对象。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
    指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
"""
# 数组
class Person:
    name = ''
    age = 0
    def __init__(self,n,ag):
        self.name = n
        self.age = ag
    def stu(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

p = Person('Eve',9)
p.stu()
p1 = Person('bob', 10)
p1.stu()

# arr = np.array([p, p1])
# print("arr:", arr)

# 遍历数组
# for i in arr:
#     print("遍历数组：", i.age)
#
# newarr = sorted(arr, key=lambda x: x.age, reverse=True)
# for i in newarr:
#     print("根据数组中的对象年龄排序：", i.name, i.age)

# 列表
# list = [p, p1]
# for i in list:
#     print("遍历列表：", i.age)
#
# list.sort(key=lambda x: x.age, reverse=True)
# for i in list:
#     print("根据列表中的对象的年龄排序:", i.name, i.age)
#

# 字典
dict = {}
dict["a"] = p
dict["b"] = p1
print("字典：", dict)
for i in dict:
    print("遍历字典：", dict[i].name, dict[i].age)
newdict = sorted(dict.items(), key=lambda x: x[1].age, reverse=True)
for i in newdict:
    print("根据字典中的对象的年龄排序：", i[1].name, i[1].age)

"""
3、遍历数组、列表，改变数组中对象的属性值
"""




"""
4、遍历数组、列表，找到满足某些条件的对象
"""




"""
5、学习怎样使用“main”方法
"""