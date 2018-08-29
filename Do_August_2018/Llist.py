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