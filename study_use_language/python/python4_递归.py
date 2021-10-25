#!/usr/bin/python
# -*- encoding=utf-8 -*-

# 把pathon路径下所有的的文件复制到E盘pathon下面去

# 1、pathon路径： os.path.dir

import os
import ntpath

# 0、目标目录
target_path = r'e:/pathon/'
if os.path.exists(target_path):
    print("目标文件路径已存在")
else:
    os.mkdir(target_path)
    print("目标文件路径已创建成功")
# 1、拿到当前文件的目录
source_path = os.path.dirname(__file__)
# source_path = r'e:/新建文件夹 (3)'
# print(source_path)  # F:/20210809/cgyi2021/study_use_language/python
# 2、拿到当文件目录的所有文件（文件+文件夹）
path_file_all = os.listdir(source_path)

# print("第一层文件夹：{0}".format(source_path))


def file_copy_every(source_path, target_path, temp):
    """
    程关依 20211024 操作问价学习
    :param temp: 判断属于第几层目录下的文件
    :param source_path: 复制路径
    :param target_path: 粘贴路径
    """
    # 1、源文件夹下所有文件
    file_list = os.listdir(source_path)
    # 2、遍历所有文件
    for file in file_list:
        file_path = os.path.join(source_path, file)  # 拿到要复制的文件
        copy_file_path = os.path.join(target_path, file)
        # 2.1判断要复制的文件是否是文件夹
        if os.path.isdir(file_path):
            temp += 1
            if os.path.exists(copy_file_path):
                file_copy_every(file_path, copy_file_path, temp)
                # print("第{1}层文件夹已存在：{0}".format(file_path, temp))  # 如果是文件夹，我就创建这个文件夹，然后递归调用自己复制
            else:
                os.mkdir(copy_file_path)
                file_copy_every(file_path, copy_file_path, temp)
                # print("第{1}层文件夹已创建：{0}".format(file_path, temp))  # 如果是文件夹，我就创建这个文件夹，然后递归调用自己复制
        else:
            # 2.1.1 如果不是文件夹，则建立读的流对象
            with open(file_path, 'rb') as read_source_file:
                source_file_n = read_source_file.read()
                # 2.1.1.1建立写对象
                with open(copy_file_path, 'wb') as write_target_file:
                    write_target_file.write(source_file_n)
                    print("{1}文件复制完成：{0}".format(file_path, temp * 4 * ' '))


file_copy_every(source_path, target_path, 0)

# print(path_file_all)
# # 3、判断当前路径是不是目录
# for file_temp in path_file_all:
#     file_path_every = os.path.join(source_path, file_temp)
#     file_path_target = os.path.join(target_path, file_temp)  # 目标路径
#     if os.path.isdir(file_path_every):
#         print("{}是目录".format(file_path_every))
#     else:
#         print("{}是文件".format(file_path_every))
#         #       4、是文件我就可以拷贝
#         #       1、读文件,然后写
#         with open(file_path_every, 'rb') as source_file_stream:
#             source_file_content = source_file_stream.read()
#             print(source_file_content)
#             with open(file_path_target, 'wb') as target_file_stream:
#                 target_file_stream.write(source_file_content)
