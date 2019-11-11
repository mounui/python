# -*- coding: utf-8 -*-
# ----------------------------------
# 请用索引取出下面list的指定元素
# ----------------------------------
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# ----------------------------------
# BMI公式(体重除以身高的平方）
# 小明身高1.75，体重80.5kg,帮小明计算他的BMI指数
# 并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# ----------------------------------
height = 1.75
weight = 80.5
bmi = weight / height ** 2
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi > 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
else:
    print('正常')

# ----------------------------------
# 计算1-100的整数之和
# ----------------------------------
sum = 0
for x in range(101):
    sum += x
print('1-100的整数之和:',sum)

# ----------------------------------
# 计算100以内所有奇数之和
# ----------------------------------
sum = 0
n = 99
while n > 0:
    sum += n
    n= n - 2
print('100以内所有奇数之和:',sum)

# ----------------------------------
# 利用循环依次对list中的每个名字打印出 Hello,xxx!
# ----------------------------------
L = ['Bart','Lisa','Adam']
for name in L:
    print('Hello,',name)

# ----------------------------------
# break和continue使用
# ----------------------------------
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# 使用break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

# 使用continue
n = 0
while n <= 99:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
