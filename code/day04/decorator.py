# -*- coding: utf-8 -*-
# ----------------------------------
# 设计一个decotator，可以作用于任何函数上并打印该函数的执行时间
# ----------------------------------
import time, functools

def metric(fn):
    start = time.time()
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        r = fn(*args, **kw)
        print('call %s() cost %5f ms:' % (fn.__name__,1000*(time.time() - start)))
        return r
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

fast(1,3)
slow(2,3,4)

# ----------------------------------
# 编写一个decorator在函数前后打印日志
# ----------------------------------

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call: %s' % func.__name__)
        c = func(*args, **kw)
        print('end call: %s' % func.__name__)
        return c
    return wrapper

@log
def now():
    print('在函数前后打印日志')

now()

# ----------------------------------
# 偏函数使用
# ----------------------------------

int2 = functools.partial(int,base=2)
print('int2(\'100000\'):',int2('100000'))
