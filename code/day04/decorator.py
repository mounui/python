# -*- coding: utf-8 -*-
# ----------------------------------
# 设计一个decotator，可以作用于任何函数上并打印该函数的执行时间
# ----------------------------------
import time, functools

def metric(fn):
    @functools.wraps(fn)
    start = time.time()
    def wrapper(*args, **kw):
        r = fn(*args, **kw)
        print('call %s() cost %5f ms:' % (fn.__name__,1000*(time.time() - start)))
        return r
    return wrapper

# 测试
@metric()
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric()
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z
