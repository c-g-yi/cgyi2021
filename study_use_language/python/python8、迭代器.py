#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    生成器是迭代的
    列表
    集合
    字典
    字符串
1、判断一个对象是否是可迭代的
    isinstance() #判断是不是这个实例
2、迭代器
    2.1：迭代是访问集合的一种方式，迭代器是一个可以记住遍历未知的对象
    2.2、迭代器对象从集合的第一个元素开始访问，知道所有的元素访问完结束
    2.2、迭代器只能往前不会后退（可以被next()函数调用并不断返回下一个值的对象成为迭代器）Interator

可迭代的 不一定是 迭代器  ：例如列表  不能被放在next()访问下一个元素
生成器是可迭代的 也是迭代器
列表是可迭代的 但不是迭代器  但是可以借助函数变成迭代器对象

生成器：为了节省内存 一个一个取到元素
迭代器：iter()：return一个迭代器
"""
# from collections import Iterable
from collections.abc import Iterable  # 这是不会报警告的用法

temp_list = [1, 2, 3]
print(isinstance(temp_list, Iterable))

f = 'asad'
print(isinstance(f, Iterable))

g = (i % 2 for i in range(0, 101))
print(isinstance(g, Iterable))

temp_list2 = [1, 1, 2, 3, 4, 5, 6]
next(g)

print(next(iter(temp_list2)))
print(next(iter(temp_list2)))
print(next(iter(temp_list2)))
print(next(iter(temp_list2)))
print(next(iter(temp_list2)))
print(next(iter(temp_list2)))
