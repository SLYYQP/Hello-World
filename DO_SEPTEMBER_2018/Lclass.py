#!/usr/bin/python
# -*- coding: UTF-8 -*-



"""
1、声明一个具有属性、方法的类
"""

class MyClass:
    i = 12345         # 类的属性
    def f(self):
        return "Hello World!"

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 是：", x.i)
print("MyClass 类的方法 f 输出是：", x.f())

"""
2、继承一个类、学习重写（覆盖）的概念
"""
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


# 多继承
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


"""
3、学习怎样声明私有属性、方法以及怎样使用它
"""



"""
4、学习静态方法、类方法、对象方法的不同
"""
# (1) 静态方法



# (2) 类的方法
#     在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self,
#     且为第一个参数，self 代表的是类的实例。

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()


# (3) 对象的方法


"""
5、学习Python的内置方法，学习在Python对象种“self”的用法
"""
# (1) self 代表类的实例，而非类
#     类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
#     self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

# self 不是 python 关键字，把他换成 runoob 也是可以正常执行的:
class Test1:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test1()
t.prt()

# (2) Python的内置方法
