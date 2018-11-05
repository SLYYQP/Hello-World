#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Dictionary字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 ":" 分割，每个键值对之间用逗号" , "分割，整个字典包括在花括号" {} "中 。

eg  :  d = {key1 : value1, key2 : value2 }

键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
字典是无序的。
"""
# create
print("..........................................Create...................................................")
# 1、创建空字典
c0 = {}
print("c0: ", c0)

# 2、直接赋值创建
c1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
c2 = {'abc': 456}
c3 = {'abc': 123, 98.6: 37}

list1 = [1, 2, 3] #练习
c4 = {1: list1, 2: c2}

print("c1:", c1)
print("c2:", c2)
print("c3:", c3)
print("c4:", c4)

# 3、通过关键字dict和关键字参数创建
c5 = dict(one=1, two=2, three=3)
print("c5:", c5)

# 4、通过二元组列表创建
list2 = [('spam', 1), ('egg', 2), ('bar', 3)]
c6 = dict(list2)
print("c6:", c6)

# 5、dict和zip结合创建
c7 = dict(zip('abc', [1, 2, 3]))
print("c7:", c7)

# 6、通过字典推导式创建
c8 = {i: 2*i for i in range(3)}
print("c8:", c8)

# 7、通过dict.fromkeys()创建，通常用来初始化字典，设置value的默认值
c9 = dict.fromkeys(range(3), 'x')
print("c9:", c9)

# 8、其他
list3 = ['x', 1, 'y', 2, 'z', 3]
c10 = dict(zip(list3[::2], list3[1::2]))
print("list3[::2]:", list3[::2], '\n', "list3[1::2]):", list3[1::2])
print("c10:", c10)

# add
print("..........................................Add...................................................")
# 1、直接赋值添加
a1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

a1['School'] = "DPS School"   # Add new entry

print("a1['School']: ", a1['School'])

# 2、如果key或value都是变量
key1 = "num"
value1 = 119876227
a1[key1] = value1

print("after 2:", a1)

# 3、setdefault方法
a1.setdefault('sex', 'male')

key2 = 'id'
value2 = '001'
a1.setdefault(key2, value2)

print("after 3:", a1)

# search
print("..........................................Search...................................................")
# 1、直接访问
s1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", s1['Name'])#把相应的键放入方括弧

# 2、
for key in s1:
    print(key, s1[key])#后面有个逗号，自动生成一个空格
    print(key + str(s1[key]))#连接两个字符串，用的是加号，直接输出，中间不加逗号

# 3、
for (k, v) in s1.items():
    print("s1[%s]=" %k, v)

# 4、get()
# 功能：通过给定的key，查找对应的value，如果给定的可以在字典中无，则返回None
# 参数：key
print("after 4:", s1.get('Name'))
print("如果给定的可以在字典中无:", s1.get("test"))

# 5、setdefault()
# 功能：通过给定的key，查找对应的value，如果给定的可以在字典中无，则返回None,
#      同时在字典中增加'test': None键值对，
# 参数：key,value
print("after setdefault:", s1.setdefault("Name"))
print("如果给定的可以在字典中无:", s1.setdefault("test_1"))
print("参数key，value：", s1.setdefault('test_2', 20))
print("s1:", s1)

# 6、python3中_contains_()替代了has_key(),用于判断键是否存在于字典中，如果键在字典中返回true，否则返回false。
print("contains:", s1.__contains__("Name"))

# modify
print("..........................................Modify...................................................")
# 1、直接修改
m1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

m1['Age'] = 8  # update existing entry

print("m1['Age']: ", m1['Age'])

# 2、update()
m2 = {'Name': 'Zara', 'Age': 7}
m3 = {'Sex': 'female' }

m2.update(m3)
print("update m2: %s" %m2)

# delete
print("..........................................Delete...................................................")
d1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del d1['Name']  # 删除键是'Name'的条目
d1.clear()  # 清空词典所有条目
# del d1  # 删除词典

print("after del d1['Name']:", d1)
print("after d1.clear():", d1)
# print("del d1:", d1)   #执行后会报错，因为del d1已经把字典删除了

# traversal
print("..........................................Traversal...................................................")
t1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# 1、先获取key，然后通过dic[key]获取value
for key3 in t1:
    print('key3 is %s , value3 is %s '%(key3, t1[key3]))

# 2、对字典items()方法返回的元组列表进行序列解包
# items()函数以列表返回可遍历的（键，值）元组数组。
for key4, value4 in t1.items():
    print('key4 is %s,value4 is %s'%(key4, value4))

# 3、遍历key值
for key5 in t1.keys():
    print(key5 + ':' + str(t1[key5]))

# 4、遍历value值
for value5 in t1.values():
    print("after 4 :", value5)

# 5、遍历字典
for kv in t1.items():
    print("after 5:", kv)

# Sort
print("..........................................Sort...................................................")
dict1 = {'a': 2, 'b': 3, 'd': 4, 'c': 8}
# 1.sorted()默认是对字典的键，从小到大进行排序
dict2 = sorted(dict1)
print("根据字典的键从小到大排序：", dict2)

# 2.也可以先拿到所有的key，然后再对key排序
list1 = sorted(dict1.keys(), reverse=True)
print("先拿到所有的key，然后再对key排序:", list1)

# 3.用dict1.values()得到所有的values，然后对value排序
list2 = sorted(dict1.values())
print("用dict1.values()得到所有的values，然后对value排序:", list2)

# 4.也可以用dict1.items()，得到包含键，值的元组
# 由于迭代对象是元组，返回值自然是元组组成的列表
# 这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键

list3 = sorted(dict1.items(), key=lambda x: x[1])
print("根据x[1]是值排序:", list3)

# 5.对键进行排序
list4 = sorted(dict1.items(), key=lambda x: x[0])
print("根据x[0]是键排序",list4)