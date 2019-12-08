# -*- coding: utf-8 -*-

print('实例属性和类属性')

class Student(object):
    name = 'Student'

s = Student()   # 创建实例s
print('s.name:',s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print('Student.name:',Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print('给实例绑定name属性:Michael并打印')
print('s.name',s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print('Student.name:',Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print('s.name',s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来

class Students(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Students.count += 1

print('test:',Students.count)
# 测试:
if Students.count != 0:
    print('测试失败!')
else:
    bart = Students('Bart')
    if Students.count != 1:
        print('测试失败!')
    else:
        lisa = Students('Bart')
        if Students.count != 2:
            print('测试失败!')
        else:
            print('Students:', Students.count)
            print('测试通过!')
