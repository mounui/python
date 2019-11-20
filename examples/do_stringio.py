# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('仰天大笑出门去\n我辈岂是蓬蒿人')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
