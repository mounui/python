# -*- coding: utf-8 -*-
# ----------------------------------
# 用filter求素数
# ----------------------------------

def primes():
    # 构造一个从3开始的奇数序列
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    # 定义一个筛选函数
    def _not_divisible(n):
        return lambda x: x % n > 0

    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 打印100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# ----------------------------------
# 利用filter筛选出回数
# ----------------------------------

# 方法一
def is_palindrome(n):
    s = str(n) # 转化成字符串
    return s == s[::-1] # 反转字符串并对比原字符串

print(list(filter(is_palindrome, range(1,1000))))

# 方法二
print(list(filter(lambda n: str(n) == str(n)[::-1],range(1,1000))))

# 方法三
def th_palindrome(n):
    s = str(n)
    h = list(range(len(s) // 2))
    for i in h:
        if s[i] != s[-(i+1)]:
            return False
    return True

print(list(filter(th_palindrome,[1231, 121, 22, 1134341, 13431])))
