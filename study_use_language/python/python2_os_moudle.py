#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

"""
    os模块里面的函数
        1、os.getcwd() ：获取当前文件夹路径
    os.path 里面的函数 __file__:当亲文件名
        1、dirname(文件路径)) 文件夹路径
        2、isabs(文件路径))   是否是绝对路径
        3、abspath(文件路径)) 文件夹路径
        4、split(文件路径)   返回一个tuple  文件夹路径+文件名及类型
        5、splitext(文件路径)    返回一个tuple   文件类型之前+文件类型
        6、getsize(文件路径)            文件大小（单位字节）
        7、join(文件夹路径,文件名)        生成文件路径
        8、exists(文件路径) 判断文件路径是否存在
        9、isdir(文件路径)   判断文件是否是一个文件夹 
    
        判断路径是否是绝对路径
"""

# 一、os模块
# 1、获取当前文件夹路径 getcwd()  不需要传递参数 返回当前文件夹路径
print(os.getcwd())
# 2、创建文件夹 mkdir(文件夹路径)
# print(os.mkdir(os.getcwd()||r'/测试目录'))
file_path_new = os.path.join(os.getcwd(), 'new_dict')
if os.path.exists(file_path_new):
    print("文件路径已存在")
else:
    print("文件路径不存在，新建文件路径")
    os.mkdir(file_path_new)
file_path = os.path.abspath(__file__)
print(file_path, '111')
os.listdir()

# 3、删除文件夹 rmdir(文件路径) :只能删除空的文件夹
# print(os.rmdir(file_path_new))
# 4、removedirs(文件路径)：删除多层文件
#
# 2、listdir(目录)  返回指定目录下的所有文件和文件夹 列表
# dict_file_list = os.listdir(os.getcwd())
# print(dict_file_list)
# for i in dict_file_list:
#     if i.is
#     print(i)


# # 二、os.path模块
# # 文件路径，
# print(os.path, type(os.path))
# # 获取当前文件所在的绝对路径
# print(os.path.dirname(__file__))
# # 当前文件夹目录 拼接文件
# file_path = os.path.join(os.path.dirname(__file__), 'os创建的文件')
#
# # os_file_temp = os.open("写文件2.txt", 'w')
# # print(os_file_temp)
#
# file_is_jdlj = os.path.isabs(r"F:\20210809\cgyi2021\study_use_language\python\简单的东西.txt")
# print(file_is_jdlj)
#
# # 当前文件的上一级 1、 isabs(参数)：是否是绝对路径
# file_is_jdlj2 = os.path.isabs('../1.txt')
# print(file_is_jdlj2)
# # file_read_temp = open("../1.txt", 'r', encoding="utf-8")
# # print(file_read_temp.readlines())
#
# # 获取文件路径    2、dirname(__file__):当前文件目录的路径directory
# file_path = os.path.dirname(__file__)
# print(file_path)
# print(os.path.isabs(file_path.join(r'/2.txt')))
# #              3、abspath(文件名)通过相对路径取得绝对路径  __file__当前文件名
# print(os.path.abspath(__file__))
# #               4、os.getcwd() 获取当前文件的文件夹路径  等价于os.path.dirname(__file__)
# print(os.getcwd())
# #               5、split(参数) 返回一个元组 文件夹路径+文件名及后缀
# file_path_split = os.path.split(os.path.abspath(__file__))
# print(file_path_split)
# #               7、splitext(参数) 返回一个元组 文件类型前面+文件类型
# file_path_split = os.path.splitext(os.path.abspath(__file__))
# print(file_path_split)
# #               8、getsize()  返回文件的字节
# file_size = os.path.getsize(os.path.abspath(__file__))
# print(file_size)
# #               9、join(路径，参数1，参数2)  拼接文件的路径
# file_size = os.path.join(os.path.dirname(__file__), r'.\a.txt')
# print(file_size)
