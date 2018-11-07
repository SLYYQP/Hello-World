# !/usr/bin/python3
# Filename: NewModule.py


# 斐波那契(fibonacci)数列模块
def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib2(n):  # 返回到 n 的斐波那契数列
    re = []
    a, b = 0, 1
    while b < n:
        re.append(b)
        a, b = b, a + b
    return re





