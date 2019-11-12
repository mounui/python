# -*- coding: utf-8 -*-

def yanghuit(n):
    res = [1]
    if n == 1:
        yield(res)
    s = 1
    while s <= n:
        if s == 1:
            yield(res)
        tmp = res
        res = []
        tmp.insert(0,0)
        tmp.append(0)
        for m in tmp:
            p = m
