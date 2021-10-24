#!/usr/bin/python
# -*- encoding=utf-8 -*-
"""
一、定义
    异常：程序运行的时候报出来的错误
    try:
        可能报异常的代码块
    except: # except  异常的类型
        报异常的代码块出现之后执行
    else:
        XXXL:当try里面没有异常会进入else  try里面不能有return
    finally:
        ddd 无论有没有异常都会进入finally

    1、最大的异常要放在最下面
    2、Exception as err 然后可以打印错误
    3、try里面有return 之后就不会执行后面的else
    4、当try里面没有异常会进入else  try里面不能有return
    5、无论有没有异常都会进入finally 以finally里面的为主
二、抛出异常
    raise Exception(异常提示信息)
"""


# 二、抛出异常
def user_login():

    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    if len(user_name) < 6:
        raise Exception("用户名必须大于6位") # Exceotion(里面就是错误的提示信息)
    else:
        print(user_name)

try:
    user_login()
except Exception as err:
    print("1111",err)
else:
    print("登录成功")
# #一、
# try:
#     number1 = int(input("请输入数字1："))
#     number2 = int(input("请输入数字2："))
#     fuhao = input("请输入运算符：")
#
#     if fuhao == '+':
#         add_value = number1 + number2
#     elif fuhao == '-':
#         add_value = number1 - number2
#     elif fuhao == '*':
#         add_value = number1 * number2
#     elif fuhao == '/':
#         add_value = number1 / number2
#     else:
#         print()
#     with open(r'F:\20210809\cgyi2021\study_use_language\python\new_dict\result_info', 'w') as write_info:
#         write_info.write(str(add_value))
#     # with open(r'F:\222313', 'r') as read_info:
#     #     read_info.read()
# except ZeroDivisionError:
#     print("除数不能为0")
# except ValueError:
#     print("输入不是数字")
# # except FileNotFoundError:
# #     print("找不到文件")
# except Exception as err:
#     print("找不到文件", err)
