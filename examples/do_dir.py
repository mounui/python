# -*- coding: utf-8 -*-

from datetime import datetime
import os

# 列出当前目录下所有文件和目录
def list_dir():
    pwd = os.path.abspath('.')

    print('     Size    Last Modefied   Name')
    print('-------------------------------------')

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d %s %s%s' %(fsize,mtime,f,flag))

# 在指定目录下查找文件并打印出相对路径
def search_file(dir,sname):
    if sname in os.path.split(dir)[1]:
        print(os.path.relpath(dir))
    if os.path.isfile(dir):
        return

    for dire in os.listdir(dir):
        search_file(os.path.join(dir,dire),sname)

search_file(r'C:\mygit','do_dir.py')
