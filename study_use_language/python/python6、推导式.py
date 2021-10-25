#!/usr/bin/python
# -*- encoding=utf-8 -*-
# 1、列表推导式 格式：[表达式 for 变量 in 旧列表]
# 找出文件列表中长度大于3并且将首字母大写
list_name = ["zs", 'ls', 'cgy', 'abcd']
list_name_shaixuan = [name.title() for name in list_name if len(name) > 2]
print(list_name_shaixuan)
# 生成1-100里面能被3整除的列表
list_temp1 = [i for i in range(1, 101) if i % 3 == 0]
print(list_temp1)
# 0-4的奇数与0-9的偶数的组合
list_temp_num = [(i, j) for i in range(0, 5) for j in range(1, 10) if i % 2 == 0 and j % 2 != 0]
print(list_temp_num)
# 列表推导式带 if else 格式
list_temp_test = [i + 100 if i == 3 else i for i in range(0, 10)]
print(list_temp_test)
# 列表推导式带 if else 格式
list_temp_test = [i + 100 if i == 3 else i for i in range(0, 10)]
print(list_temp_test)

# 2、字典推导式 {key:value for key,value in 字典.items()}
dict_temp = {"a": 1, "b": 2, "c": 3, "d": 4, "f": 5}
dict_result = {j: i for i, j in dict_temp.items()}
print(dict_result)
# 3、集合推导式 雷士列表推导式，在列表推倒时的基础上添加了一个去重重复项
list = [1, 2, 23, 1, 31, 3, 12, 3, 123, 123, 1213]
set_temp = {i + 1 for i in list}
print(set_temp)
# 4、元组推导式，---》生成器 小括号