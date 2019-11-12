# -*- coding: utf-8 -*-

#-----------------------------------
# 使用迭代查找一个list中最小和最大值
#-----------------------------------

def findMinAndMax(L):
    m = 0
    n = 0
    for v in L:
        s = int(v)
        if n == 0:
            n = s
        if s > m:
            m = s
        elif s < n:
            n = s
    return (n,m)

