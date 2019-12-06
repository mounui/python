# -*- coding: utf-8 -*-
# 计算所有参数乘积

def product(*param):
    s = 1
    for a in param:
        s *= a
    return s

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7,9) =', product(5, 6, 7, 9))
