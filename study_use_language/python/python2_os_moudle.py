#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# 文件路径，
print(os.path)
print(os.path, type(os.path))
# 获取当前文件所在的绝对路径
print(os.path.dirname(__file__))
# 当前文件夹目录 拼接文件
file_path = os.path.join(os.path.dirname(__file__),'os创建的文件')

os.w


# os_file_temp = os.open("写文件2.txt", 'w')
# print(os_file_temp)
