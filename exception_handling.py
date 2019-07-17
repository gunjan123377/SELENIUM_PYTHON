# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# def foo():
#     try:
#         print("Gunjan")
#     finally:
#         return 2
# k = foo()
# print(k)

# def foo():
#     try:
#         return "Gunjan"
#     finally:
#         return 2
# k = foo()
# print(k)

# f=open("youtube_download.py")
# print(f.readline())
# print(f.readline())
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.read(20))
# print(f.tell())
# print(f.seek(0,0))
# print(f.read(20))


import time
from datetime import datetime
import os
# print(os.getcwd())
# print(os.listdir('D:\sel_py_training'))
# os.chdir('D:\sel_py_training')
# os.mkdir('Demo')
# os.makedirs('Demo\guntest')
# time.sleep(2)
# # os.rmdir('Demo')
# os.removedirs('Demo\guntest')
# # os.rename('old.txt','new.txt')
print(os.stat('geckodriver.log'))
print(datetime.fromtimestamp(os.stat('geckodriver.log').st_mtime))
for dirpath, dirnames, filenames in os.walk('D:\sel_py_training'):
    print(dirpath)
    print(dirnames)
    print(filenames)
