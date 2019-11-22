# -*- coding: utf-8 -*-

import re

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:',t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

def is_valid_email(addr):
    if (re.match(r'[a-zA-Z0-9\.\@]+',addr)):
        print('success')
    else:
        print('fail')

# 测试:
is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
not is_valid_email('bob#example.com')
not is_valid_email('mr-bob@example.com')
