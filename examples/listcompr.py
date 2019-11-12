# -*- coding: utf-8 -*-
 
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'a': 'M', 'b': 'N'}
print([k + '=' + v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
