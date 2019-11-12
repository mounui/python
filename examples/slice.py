# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3]:',L[0:3])
print('L[:3]:',L[:3])
print('L[1:3]:',L[1:3])
print('L[-2:]:',L[-2:])

R = list(range(100))
print('R[:10]:',R[:10])
print('R[-10:]:',R[-10:])
print('R[10:20]:',R[10:20])
print('R[:10:2]:',R[:10:2])
print('R[::5]:',R[::5])

#-------------------------------
# 用切片实现trim函数
#-------------------------------

def my_trim(s):
    while(True):
        if (s[:1] != ' ' and s[-1:] != ' '):
            return s
        elif s[:1] == ' ':
            s = s[1:]
        elif s[-1:] == ' ':
            s = s[:-1]
    return s
