#!/usr/bin/python
# -*- coding: UTF-8 -*-

# data = [x for x in range(10, 20)]
# print(data)
# sum = 0
# for x in data:
#     sum = sum + x
#
# print(sum)
#
# """
# 1、字典赋值的操作是用中括号进行的，若有某个元素会更新，若没有则会新增；
# 2、字符串的拼接，类型要匹配，整型不能和字符串拼接。
# """
# dict = {}
# for x in data:
#     dict[str(x)] = "第" + str(x) + "个"
# print(dict["10"])
# print(dict)

# from DO_SEPTEMBER_2018 import NewModule
# NewModule.fib(100)

from DO_SEPTEMBER_2018 import fib
fib(100)
