# -*- coding: utf-8 -*-

import itertools

def pi(N):
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x % 2 == 1, natuals)
    p,s = 1,0
    for i in ns:
        if i > 2 * N - 1:
            break
        s += (4/i)*p
        p = -p
    return s

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
