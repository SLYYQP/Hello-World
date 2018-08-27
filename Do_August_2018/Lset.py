#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
集合（set）是一个无序不重复元素的序列。

可以使用大括号 { } 或者 set() 函数创建集合。

注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

# create
print("..........................................Create...................................................")
# 1、创建一个空集合
c1 = set()

print("c1:", c1)

# 2、直接赋值
c2 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
c3 = set('apple')

print("c2:", c2)
print("c3:", c3)

# 3、
c4 = set(c2)

print("c4:", c4)

# add
print("..........................................Add...................................................")
# 1、s.add( x )，将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
a1 = set(("Google", "Runoob", "Taobao"))
a1.add("Facebook")

print("a1:", a1)

# 2、s.update( x )，也可以添加元素，且参数可以是列表，元组，字典等。
# x可以有多个，用“，”分开。
a1.update({1, 3})
print("after update:", a1)

a1.update([1, 4], [5, 6])
print("after update list:", a1)

# search
print("..........................................Search...................................................")
# 判断元素s是否在集合x中存在，存在返回True，不存在返回False。
s1 = set(("Google", "Runoob", "Taobao"))

print("Taobao" in s1)
print("Facebook" in s1)

# delete
print("..........................................Delete...................................................")
# 1、s.remove( x )，将元素x添加到集合s中移除，如果元素不存在，会发生错误。
d1 = set(("Google", "Runoob", "Taobao"))
d1.remove("Taobao")

print("after remove:", d1)

# 2、s.discard( x ),如果元素不存在，不会发生错误。
d1.discard("Facebook")
print("after discard:", d1)

# 3、s.pop(),随机删除集合中的一个元素。
d1.pop()
print("after pop:", d1)

# 4、s.clear(),清空集合
d1.clear()
print("after clear:", d1)

# traversal
print("..........................................Traversal...................................................")
t1 = set(("Google", "Runoob", "Taobao"))

for i in t1:
    print(i)

t2 = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

for x in t2:
    print(x)