# -*- coding: utf-8 -*-
# ----------------------------------
# 利用切片操作去除字符串首尾空格
# ----------------------------------

def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    return s

# str = input('请输入字符串：')
str = ' hello world   '
print(str)
print(trim(str))

# ----------------------------------
# 使用迭代查找一个list中的最小和最大值并返回一个tuple
# ----------------------------------

def findMinAndMax(L):
    if L != []:
        (max,min) = (L[0],L[0])
        for v in L:
            if v > max:
                max = v
            if v < min:
                min = v
        return(min,max)
    else:
        return(None, None)

L = [1,3,4,5,2,8]
print(findMinAndMax(L))

# ----------------------------------
# 斐波拉契数列
# ----------------------------------

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# ----------------------------------
# 杨辉三角
# ----------------------------------

def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# ----------------------------------
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# ----------------------------------

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# ----------------------------------
# 接受一个list并求积
# ----------------------------------
from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([1,3,5,9]))

# ----------------------------------
# 把字符串转换成浮点数 eg:'123.456'
# ----------------------------------

def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    # 从小数点处将字符串拆分为前后两段
    int_str, float_str = s.split('.')
    return reduce(fn, map(char2num, int_str)) + reduce(fn, map(char2num, float_str)) / pow(10, len(float_str))

print('str2float(\'123.456\') =', str2float('123.456'))
