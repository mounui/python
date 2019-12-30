# -*- coding: utf-8 -*-
import psutil
print('cpu逻辑数量：',psutil.cpu_count())
print('CPU物理核心：',psutil.cpu_count(logical=False))
print('统计CPU的用户/系统/空闲时间：',psutil.cpu_times())

