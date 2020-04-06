# -*- coding: utf-8 -*-
import math
# ----------------------------------
# 定义函数检查参数类型
# ----------------------------------

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
# ----------------------------------
# 一元二次方程的两个解
# ----------------------------------

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1,x2

print(quadratic(2,3,1))

# ----------------------------------
# 计算多个数的乘积
# ----------------------------------

def product(*args):
    s = 1
    for i in args:
        s *= i
    return s

print(product(5))
print(product(5,6))
print(product(5,6,7))

# ----------------------------------
# 汉诺塔实现
# ----------------------------------

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)

hanoi(5, 'A', 'B', 'C')

