#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
字符串是 Python 中最常用的数据类型。可以使用引号('或")来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。
"""

# create
print("..........................................Create...................................................")
c1 = 'Hello World!'
c2 = "Hello Python!"

print("c1:", c1)
print("c2:", c2)

# search
print("..........................................Search...................................................")
# Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
# Python访问子字符串，可以使用方括号来截取字符串。

print("c1[0]:", c1[0])
print("c2[1:5]:", c2[1:5])

# update
print("..........................................Update...................................................")
# 可以对已存在的字符串进行修改，并赋值给另一个变量。
u1 = c1[:6] + "Facebook"
print("更新字符串：", u1)

# concat
print("..........................................Concat...................................................")
# 1、直接通过“+”拼接
# 使用简单直接，但是网上不少人说这种方法效率低
# 之所以说python 中使用 + 进行字符串连接的操作效率低下，是因为python中字符串是不可变的类型，
# 使用 + 连接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，当连续相加的
# 字符串很多时(a+b+c+d+e+f+...) ，效率低下就是必然的了.

con1 = "I" + "Love" + "Python"

print("con1:", con1)

# 2、join方法
# 使用略复杂，但对多个字符进行连接时效率高，只会有一次内存的申请。而且如果是对list的字符进行连接的时候，这种方法必须是首选.
list1 = ['You', 'Love', 'Java']
con2 = ''.join(list1)

print("con2:", con2)

# 3、替换,字符串格式化，这种方法非常常用
con3 = '%s%s%s'%('He', 'Love', 'Python')

print("con3:", con3)

# split
print("..........................................Split...................................................")
# 1、split()函数应该说是分割字符串使用最多的函数
s1 = "Hello,python,Good Night"
s2 = s1.split(',')
s3 = s1.split()

print("s2:", s2)
print("s3:", s3)

# 2、splitline()函数是按“行”进行字符串分割
# a.如果对象s4中除了换行符，字符串前后还有空格的话，可以用strip()函数去除字符串前后的空格
# b.对于splitlines()函数有一个keepends的bool型参数，当keepends为True时：分割的每 一行里尾部会有\n；
# 当keepends为False时：不保留每行结尾的\n；
s4 = """I have a pen
        I have a apple
        apple pen
     """
s5 = s4.splitlines()

print("s5:", s5)

# 3、import re模块 进行字符串多种字符的分割，在处理某些字符串的时候，需要在一个字符串中进行多个字符的分割，
# 但是对于第一种方法split()一次只可以使用一个符号进行字符串分割操作
#先导入re模块：import re
#之后：re.split('分割符1|分割符2'，objects) --> 不同的分割符用 ‘|’ 进行间隔(分割符需要进行'\'的转义操作)，
# 然后objects为需要分割的字符串对象。
#注意: '.' 这个分割符进行了 '\.' 的转义表示 '.' 进行分割。
s6 = "852317006@qq.com"
import re
re.split('@|\.', s6)

print("after import re:", re.split('@|\.', s6))

# replace
print("..........................................Replace...................................................")
# replace(old, new [, max])
# 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
r1 = "I love Java"
r2 = r1.replace("Java", "Python")

print("r2:", r2)

# operation
print("..........................................Operation...................................................")
# 1、复制字符串
str1 = "strcpy1"
str2 = str1
str1 = "strcpy2"

print("str2:", str2)

# 2、连接字符串1、2
str3 = "strcat"
str4 = "append"
str3 += str4

print("str3:", str3)

# 3、查找字符串1、2
str5 = "strchr"
str6 = 'p'
# str7 = str5.index(str6)

# print("str7:", str7)  # 报错

str8 = str5.find(str6)  # < 0为未找到
print("str8:", str8)

# 4、比较字符串，python3中没有cmp函数
import operator as op
str9 = 'strchr'
str10 = 'strch'
n = 3

print("比较：", op.eq(str9, str10))
print("字符串指定长度比较：", op.eq(str9[0:n], str10[0:n]))

# 5、扫描字符串是否包含指定的字符
str11 = '12345678'
str12 = '456'

print("after scan", len(str11 and str12))

# 6、字符串长度
print("strlen", len(str11))

# 7、将字符串中的大小写转换
str13 = "JCstrlwrHELLO"
str14 = str13.capitalize()

print("str14:", str14)

# 8、追加指定长度的字符串
str15 = '12345'
str16 = 'abcdef'
n = 3
str15 += str16[0:n]
print("str15", str15)

# 9、将字符串前n个字符替换为指定的字符
str16 = '12345'
ch = 'r'
n = 3
str16 = n * ch + str16[3:]

print("str16:", str16)

# 10、翻转字符串
str17 = 'abcdefg'
str17 = str17[::-1]

print("str17:", str17)
