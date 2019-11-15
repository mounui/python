# -*- coding: utf-8 -*-
# super使用 避免基类多次调用

class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

C()

# 测试结果
# enter C
# enter A
# enter B
# enter Base
# leave Base
# leave B
# leave A
# leave C
