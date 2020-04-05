print('hello world!')

name = input('please enter your name:')
print('hello,',name)

print(1024 * 768)

print(5^2)

print('haha')

bmi = 80.5 / (1.75 ** 2)
if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')

sum = 0
for x in range(101):
    sum += x

print(sum)
