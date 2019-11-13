# -*- coding: utf-8 -*-

# 下面的tuple表示用户姓名和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 用sorted按照名字排序

def by_name(t):
    return t[0].lower()

print('按照姓名排序',sorted(L, key=by_name))

# 用sorted按照成绩排序

def by_score(t):
    return t[1]

print('按照成绩排序',sorted(L, key=by_score))
