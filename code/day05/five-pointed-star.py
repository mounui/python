# -*- coding: utf-8 -*-
# ----------------------------------
# 海龟绘图 画一个五角星
# ----------------------------------
from turtle import *

def darwStar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    darwStar(x, 0)

done()
