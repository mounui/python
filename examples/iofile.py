# -*- coding: utf-8 -*-

import datetime

# 读文件
f = open('C:\Windows\win.ini','r')
print(f.readlines())
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
try:
    f = open('C:\Windows\win.ini','r')
    print(f.read())
finally:
    if f:
        f.close()

# 二进制文件
#with open(r'C:\Windows\fzf.exe','rb') as f:
#    print(f.read())

# 写文件
with open('iofile.txt','w') as t:
    t.write('Hello, world!')

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
