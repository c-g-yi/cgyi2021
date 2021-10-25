#!/usr/bin/python
# -*- encoding=utf-8 -*-
"""
genarator定义
1、列表推导式得到一个生成器
     注意小括号就是生成器，中括号就是生成一个列表
     格式：
         g= (表达式1 if 条件 else 表达式2 for i in 迭代器)
         g= (表达式1 表达式2 for i in 迭代器 if 条件)
         g= (表达式1 表达式2 for i in 迭代器)

2、【函数带yiled的就是生成器】
    格式：
        def 函数名(参数):
            number = 0
            while True:
                number += 1
                yiled number  # yiled就是在这里给返回一个值+暂停

genarator产生元素
    获取生成器的下一个元素 ，不能忘里面传值
    next()
    __next__()

send(value)：每次调用生成器中传值

**********************应用：协程**********************
"""


def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        for x in range(0, temp):
            print(x,end=' ')
        i += 1
    return "生成器没有更多元素"


temp_interation = test()
# print(next(temp_interation))
# print(next(temp_interation))
# print(next(temp_interation))
# print(temp_interation.__next__())
print(temp_interation.send(None))
print(temp_interation.send(3))
print(temp_interation.send(10))

# 生成器
# 通过列表推导式得到生成器
# list_temp = (i for i in range(0, 10) if i % 3 == 0)
# print(list_temp)


# print(len(list_temp))
# 1、获取生成器里面的数据 __next__()
# print(list_temp.__next__())
# print(list_temp.__next__())
# print(list_temp.__next__())
# print(list_temp.__next__())
# # next(生成器对象) 系统内置函数
# print(next(list_temp))
#
# print(next(list_temp))
# print(next(list_temp))
# StopIteration 生成器里面的元素遍历完了之后  会抛出异常、


# while True:
#     try:
#         e = next(list_temp)
#         print(e)
#     except Exception as err:
#         print("wocuole ", err)
#         break
#     else:
#         print("我是else 我的值是{0}".format(e))
#     finally:
#         print("生成器还有值，我是finally")


# def func():
#     n = 0
#     while True:
#         n += 1
#         # print(n) 函数中出现了yield关键字，说明函数就不是函数了，就是一个生成器  【return + 暂停】
#         yield n
#
#
# func_duiiang = func()
# print(func_duiiang)


# # 斐波拉切数列
# def fib(lenth):
#     a, b = 0, 1
#     n = 0
#     while n < lenth:
#         # print(b)
#         yield b # 返回 B 并暂停
#         a, b = b, a + b
#         n += 1
#     return "超过生成器最大生成数"  # 就是在得到StopIteration当做错误消息来警醒提示
# d = fib(8)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
