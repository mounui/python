# -*- coding: utf-8 -*-

#-----------------------------
# 删掉偶数只保留奇数
#-----------------------------

def is_odd(n):
    return n % 2 == 1

L = range(100)

print('保留list中的奇数',list(filter(is_odd,L)))

#-----------------------------
# 删掉list中的空字符串
#-----------------------------

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',' '])))

#-----------------------------
# 素数
#-----------------------------

def primes():
    def _odd_iter():
        n = 1
        while True:
            n += 2
            yield n

    def _not_divisible(n):
        return lambda x: x % n > 0

    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

print('1000以内的素数')
main()

#-----------------------------
# 回数
#-----------------------------
def is_palindrome(n):
    return str(n)==str(n)[::-1]
     
print('1000以内的回数',list(filter(is_palindrome, range(1, 1000))))
