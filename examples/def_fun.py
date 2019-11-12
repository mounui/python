# -*- coding: utf-8 -*-

import math

def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move (x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print('my_abs(-20):',my_abs(-20))

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a,b,c):
    n = math.sqrt(b ** 2 - 4 * a * c)
    x = (-b + n) / (2 * a)
    y = (-b - n) / (2 * a)
    return x, y

print('quadratic(2,3,1):',quadratic(2,3,1))
print('quadratic(1,3,-4):',quadratic(1,3,-4))
