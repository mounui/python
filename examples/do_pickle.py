# -*- coding: utf-8 -*-

import pickle, json

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

print('json:')

data = json.dumps(d)
print('JSON Data is a str:',data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s,default=lambda obj:obj.__dict__)
print('Dump Student:',std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'],d['age'],d['score']))
print(rebuild)

print('dumps参数ensure_ascii')
obj = dict(name='小明',age=20)
s = json.dumps(obj, ensure_ascii=True)
print('True:',s)
s = json.dumps(obj, ensure_ascii=False)
print('False:',s)
