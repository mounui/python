# -*- coding: utf-8 -*-

from functools import reduce

#----------------------------
# 对一个list求累积
#----------------------------

def mix(x,y):
    return x * y

def prod(L):
    return reduce(mix,L)

print('prod([1,2,3,4,5]):',prod([1,2,3,4,5]))

#----------------------------
# 利用map和reduce编写一个str2float函数
#----------------------------

def str2float(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(fn,s1) + reduce(fn,s2) / 10 ** len(s2)


print('str2float(\'123.456\')=',str2float('123.456'))
