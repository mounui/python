# -*- coding: utf-8 -*-

import time, threading

# 假定这是你的银行存款：
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0：
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

def run_thread_lock(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            # 修改
            change_it(n)
        finally:
            # 修改完一定要释放锁
            lock.release()
        
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('nolock:',balance)

balance = 0
t3 = threading.Thread(target=run_thread_lock, args=(5,))
t4 = threading.Thread(target=run_thread_lock, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print('lock',balance)
