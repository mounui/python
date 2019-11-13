# -*- coding: utf-8 -*-

import time, functools

#-----------------------------
# 设计一个装饰器，可以作用在任何函数上
# 并打印该函数的执行时间
#-----------------------------

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print("%s runned in %.4f seconds" % (fn.__name__,end-start))
        return res
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11,22)
s = slow(11,22,33)
if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')

