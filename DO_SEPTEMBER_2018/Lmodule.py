#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename:Lmodule

# import NewModule                                  # 一般工程上不用这种方法

from DO_SEPTEMBER_2018.NewModule import fib, fib2  # 1
# from DO_SEPTEMBER_2018 import NewModule           # 2
# from DO_SEPTEMBER_2018 import *                  # 3

# from . import NewModule   ?


"""
1、创建一个有一些类、方法、变量的模块
"""


# 斐波那契(fibonacci)数列模块
# def fib(n):  # 定义到 n 的斐波那契数列
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
#     print()
#
#
# def fib2(n):  # 返回到 n 的斐波那契数列
#     re = []
#     a, b = 0, 1
#     while b < n:
#         re.append(b)
#         a, b = b, a + b
#     return re

"""
2、创建一个新的模块用来使用上一步声明的类、变量和方法，新模块“NewModule”
"""
# 1
fib(1000)
print(fib2(100))

# 2
# NewModule.fib(1000)
# print(NewModule.fib2(100))
# print(NewModule.__name__)



# 3 "from DO_SEPTEMBER_2018 import *",后面有“×”号，需要在__init__中写“__all__=['Lmodule','NewModule']”，
#   表示在“DO_SEPTEMBER_2018”包中使用NewModule模块。否则会导入“DO_SEPTEMBER_2018”包中的所有".py"文件。
# NewModule.fib(100)


# 当在“DO_SEPTEMBER_2018”包外使用包内的模块时，需要在__init__中添加“from .NewModule import fib, fib2”。
# 在包外这样使用：
# from DO_SEPTEMBER_2018 import NewModule
# NewModule.fib(100)


# 当在“DO_SEPTEMBER_2018”包外使用包内的模块时，需要在__init__中添加“from . import fib”。
# 在包外这样使用：
# from DO_SEPTEMBER_2018 import fib
# fib(100)


