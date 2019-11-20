# -*- coding: utf-8 -*-

from io import BytesIO

# write to BytesIO:
f= BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '桃花潭水深千尺，不及汪伦送我情'.encode('utf-8')
f = BytesIO(data)
print(f.read())
