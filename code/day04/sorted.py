# -*- coding: utf-8 -*-
# ----------------------------------
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 用sorted对以上学生信息按照名字排序
# ----------------------------------

def by_name(t):
    return t[0].lower()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=by_name))

print(sorted(L, key=lambda x: x[0].lower()))

# 按成绩从高到低排序
print(sorted(L, key=lambda x: x[1], reverse=True))

# ----------------------------------
# 返回函数
# ----------------------------------

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# ----------------------------------
# 利用闭包返回一个计数器
# ----------------------------------

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

counterA = createCounter()
print(counterA())
print(counterA())
print(counterA())

def createCounterT():
    def f():
        x = 0
        while True:
            x = x + 1
            yield x
    sum = f()
    def counter():
        return next(sum)
    return counter

def createCounterH():
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter

# ----------------------------------
# 匿名函数 关键字：lambda
# ----------------------------------

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
# 改成匿名函数如下
N = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print('L:',L)
print('N:',N)
