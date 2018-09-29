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
# (1) __private_attrs：两个下划线开头，声明该属性为私有，
#     不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

# (2) __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用，
#     不能在类地外部调用。self.__private_methods。
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错,外部不能调用私有方法


"""
4、学习静态方法、类方法、对象方法的不同
   python中实现静态方法和类方法都是依赖于python的修饰器来实现的。 
   对象方法有self参数，类方法有cls参数，静态方法是不需要这些附加参数的。
   
   注意:方法的第一个参数都是类对象而不是实例对象. 
   按照惯例,类方法的第一个形参被命名为 cls.任何时候定义类方法都不是必须的
  （类方法能实现的功能都可以通过定义一个普通函数来实现,只要这个函数接受一个类对象做为参数就可以了）。
"""
# (1) 静态方法
#     要在类中使用静态方法，需在类成员函数前面加上 @staticmethod 标记符，以表示下面的成员函数是静态函数。
#     使用静态方法的好处是，不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法。

# (2) 类方法
#     类方法与普通的成员函数和静态函数有不同之处，在接触的语言中好像也没见过这种语义，看它的定义：
#     一个类方法就可以通过类或它的实例来调用的方法, 不管你是用类来调用这个方法还是类实例调用这个方法,
#     该方法的第一个参数总是定义该方法的类对象。

# (3) 对象的方法
#     类/对象可以拥有像函数一样的方法，这些对象方法与函数的区别只是一个额外的 self 变量
class Person:
    grade = 1

    def __init__(self, name):
        self.name = name

    def sayHi(self):  # 加self区别于普通函数
        print('Hello, your name is?', self.name)


    @staticmethod  # 声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def sayName():  # 使用了静态方法，则不能再使用self
        print("my name is king")   # ,grade, #self.name

    @classmethod  # 类方法
    def classMethod(cls):
        print("class method")


p = Person("king")
p.sayHi()
p.sayName()
p.classMethod()
Person.classMethod()


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
"""
类的专有方法:

    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方

    Python同样支持运算符重载，可以对类的专有方法进行重载。
"""