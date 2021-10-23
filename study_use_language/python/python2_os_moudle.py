#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

"""
    os模块
    
    os.path 
    
        判断路径是否是绝对路径
"""
# 文件路径，
print(os.path)
print(os.path, type(os.path))
# 获取当前文件所在的绝对路径
print(os.path.dirname(__file__))
# 当前文件夹目录 拼接文件
file_path = os.path.join(os.path.dirname(__file__), 'os创建的文件')

# os_file_temp = os.open("写文件2.txt", 'w')
# print(os_file_temp)

file_is_jdlj = os.path.isabs(r"F:\20210809\cgyi2021\study_use_language\python\简单的东西.txt")
print(file_is_jdlj)
