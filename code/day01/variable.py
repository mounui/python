"""
使用input()函数获取键盘输入（字符串）
使用int()函数将输入的字符串装换成整数
使用print()函数输出带占位符的字符串
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))


a = 10
b = 3
a += b
a *= a + 2
print(a)

# 将华氏温度转换为摄氏温度

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

# 输入年份判断是不是闰年

year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
