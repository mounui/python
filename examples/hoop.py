# -*- coding: utf-8 -*-

# 限制实例属性 特殊变量__slots__
print('限制实例属性:','__slots__')

class Student(object):
    __slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称

s = Student()   # 创建新的实例
s.name = 'Mao'
s.age = 18
# s.score = 99
# ERROR: AttributeError: 'Student' object has no attribute 'score'

# @property
print('@property')

class Pstudent(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

p = Pstudent()
p.score = 60
print('p.score:',p.score)

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must be > 0')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
