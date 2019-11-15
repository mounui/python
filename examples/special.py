# -*- coding: utf-8 -*-

# __str__
print('__str__使用')

class Demostr(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Demostr object (name: %s)' % self.name

    __repr__ = __str__

t = Demostr('mao')
print(t)
t

# __iter__
print('__iter__使用')

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a, b

    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:   # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

# 测试
print('斐波那契数列')
for n in Fib():
    print(n)


# __getitem__
print('__getitem__使用')

class Fiba(object):
    
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+ b
        return a

f = Fiba()
print(f[0])
print(f[1])
print(f[10])

class Fibs(object):
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fibs()
print('f[:10]:',f[:10])


# __getattr__
print('__getattr__使用')

class Demogtr(object):

    def __init__(self):
        self.name = 'Mao'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25

s = Demogtr()
print('s.name:',s.name)
print('s.score:',s.score)
print('s.age():',s.age())

# __call__
print('__call__使用')

class Democall(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Democall('Mao')
s()

print(callable(s))
print(callable(max))
print(callable(None))
