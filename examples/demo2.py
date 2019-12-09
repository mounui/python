print('''line1
line2
line3''')

print(r'''hello,\n
world''')

print(r'hello \'\n world')

a = 123     # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
Lisa!'''
print('n =',n)
print('f =',f)
print('s1 =',s1)
print('s2 =',s2)
print('s3 =',s3)
print('s4 =',s4)

print(ord('A'))  # 获取字符的整数表示
print(ord('中'))
print(chr(66))  # 把编码转换为对应的字符
print(chr(25991))

s1 = 72
s2 = 85
res = (s2 - s1) / s1 * 100
print(res)
print('成绩提升百分比：%.1f' % res)
