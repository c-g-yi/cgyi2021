#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进程》线程》携程(生成器)
"""
进程：

线程：

携程：
"""


def task1(n):
    for i in range(n):
        print("{}几块".format(i))
        yield None


def task2(n):
    for i in range(n):
        print("听歌{}".format(i))
        yield None


g1 = task1(10)
g2 = task2(10)

i = 0
while True:
    try:
        # if i % 2 == 0:
        #     i += 1
        #     g1.__next__()
        # else:
        #     i += 1
        #     next(g2)
        g1.__next__()
        next(g2)
    except Exception as err:
        break
    # else:
    #     print("我是else")
    #     break
    # finally:
    #     print("我是finally")
    #     break
