# -*- coding: utf-8 -*-

#-------------------------------
# 返回一个闭包函数，每次调用数值增加1
#-------------------------------

def createCounter():
    n = [0]
    def counter():
        while True:
            n[0] = n[0] + 1
            return n[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
