#!/usr/bin/python
# -*- encoding=utf-8 -*-

# 生成器
# 通过列表推导式得到生成器
list_temp = (i for i in range(0, 10) if i % 3 == 0)
print(list_temp)
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


def func():
    n = 0
    while True:
        n += 1
        # print(n) 函数中出现了yield关键字，说明函数就不是函数了，就是一个生成器
        yield n

func_duiiang = func()
print(func_duiiang)