# -*- coding: utf-8 -*-
# ----------------------------------
# __slots__限制实例属性的用法
# ----------------------------------

# 先定义一个class
class Student(object):
    pass

# 实例化并绑定一个属性
s = Student()
s.name = 'Mao'
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(18)
s.age

# 给实例绑定方法对另一个实例式不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

# 如果我们想要限制实例属性，可以定义一个特殊的__slots__变量
class Student(object):
    __slots__ = ('name', 'age')

# 使用__slots__定义的属性仅对当前实例起作用，对继承的子类是不起作用的
# 除非在之类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
