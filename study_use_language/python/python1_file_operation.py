#!/usr/bin/python
# -*- encoding=UTF-8 -*-

"""
1、获取读、写的对象
open（文件路径 ， '读取模式'，文件编码）
    文件路径：
        1、文件路径（绝对路径）
        2、文件名(同级目录文件名就行)
        3、相对路径
    读取模式：
        1、读
            1.1、r   当读的是路径有误，代码会报错
            1.2、
        2、写
            2.1、w   写的时候路径有误会新建文件
            2.2、a   追加   ****特殊写追加模式****
        3、
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    文件编码
        1、GBK
        2、unionde
        3、UTF-8
2、读、写可调用的方法：
    read(n) 读n个字节
    readline() 读一行
    readlines() 读取所有的行 返回一个可迭代对象
    readable() 是否可读 是true否false

    write()     不换行写
    wtiteline() 换行写
    writeable()：是否可写  是true否false

    close()关闭流对象
"""
# 1、读
# file_temp_read = open("F:/20210809/cgyi2021/study_use_language/1.txt", 'rb')
# read(30)读多少个字节
# print(file_temp_read.read(30))
# readline()读一行
# print(file_temp_read.readline())
# readlines()读多行，返回是一个对象
# print(file_temp_read.readlines())
# 遍历可迭代对象获取文件
# for i in file_temp_read_read.readlines():
#     print(i, end=' ')
# readable()判断文件是不是可读的
# print(file_temp_read.readable())

# # 二、写
# file_temp_write = open("D:/cgyi2021/study_use_language/python/2.txt", 'ab')
# # 判断文件是否能读取
# if file_temp_write.writable():
#     for file_cone in file_temp_read.readlines():
#         file_temp_write.write(file_cone)
# else:
#     print("文件不可写")
# # file_temp_write.write(2)
#
# file_temp_write.close()
# file_temp_read2 = open("D:/cgyi2021/study_use_language/python/不可读文件.txt", 'r')
# print(file_temp_read2.readable())

# file_add_content = open("")