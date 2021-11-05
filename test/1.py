#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""  # OS

import os
import ntpath

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)  # nt Windows系统。
evi = os.environ
# print(type(evi))
# for i in str(evi).split(','):
#     print(i)
# print(os.getcwd())
print(os.listdir)
for i in os.listdir():
    print(i)
# print(os.mkdir('程关依.txt'))
# print(os.rmdir('程关依.txt'))
# print(os.remove("中国.txt"))
#  OS 文件列表 listdir()  当前路径getcwd() 创建文件夹mkdir()  删除空文件夹rmdir()  删除文件remove() 重命名rename()
# OS.path

list_type = [file_type for file_type in os.listdir('.') if os.path.splitext(file_type)[1] == '.py']
print(list_type)

file_path = os.getcwd()
print(file_path)
print(os.path.isabs(file_path))  # 判断路径是否是全路径
print(os.path.isdir(file_path))  # 判断是否是一个目录
print(os.path.abspath(__file__))  # 文件的绝对路径
print(os.path.dirname(__file__))  # 文件夹路径
file_path2 = os.path.dirname(__file__)
print(file_path2)
print(os.path.isabs(file_path2))  # 判断路径是否是全路径
print(os.path.split(os.path.abspath(__file__)))    # 切割文件  文件夹路径和文件名
print(os.path.splitext(os.path.abspath(__file__))) # 切割文件  文件夹+文件名  ,文件类型
"""
# 一、open()
file_path = r'D:\cgyi20211025\study_use_language\python\简单的东西.txt'
file_path_write = r'D:\cgyi20211025\test\2025.txt'
file_stream_read = open(file_path, 'r', encoding='UTF-8')
file_stream_write = open(file_path_write, 'a', encoding='utf-8')

print(file_stream_read.name, file_stream_read.mode, file_stream_read.encoding, file_stream_read.buffer)
print(file_stream_write.name, file_stream_write.mode, file_stream_write.encoding, file_stream_write.buffer)
print(file_stream_read.__sizeof__())
# 读全部read()  读多少个字节read(n)  读一行readline， 读所有行列表readlines  判断文件是否可读readable 文件大写readsize()
# 注意文件不存在 读文件会报错  需要通过
# 写字符串writer  序列writelines(seq)

try:
    file_stream_read2 = open(r'D:\cgyi20211025\test\20251.txt', 'r')
    print("try执行异常代码之后会不会执行")
except Exception as err:
    print(err)
    print("except执行异常代码之后会不会执行")
else:
    print("else报错之后else会不会执行")
finally:
    print("finally执行异常代码之后会不会执行")
"""
