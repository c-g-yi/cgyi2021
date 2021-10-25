#!/usr/bin/python
# -*- encoding=utf-8 -*-

# 1注册
def guan_register():
    print("欢迎注册“关”系统")
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    password2 = input("请再次输入密码：")
    if password == password2:
        with open(r'F:\20210809\cgyi2021\study_use_language\python\new_dict\user_info_tab.txt', 'a',
                  encoding='utf-8') as write_user_info:
            write_user_info.write('{} {}\n'.format(user_name, password))
    else:
        print("两次密码不一致，请重新输入")
        guan_login()


# 2登录
def guan_login():
    print("欢迎登录“关”系统")
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    password2 = input("请再次输入密码：")
    if password == password2:
        user_input_info = '{} {}\n'.format(user_name, password)
        with open(r'F:\20210809\cgyi2021\study_use_language\python\new_dict\user_info_tab.txt', 'r',
                  encoding='utf-8') as red_user_info:
            for user_info in red_user_info.readlines():
                if user_info == user_input_info:
                    print("'关'系统登录成功，欢迎{0}使用".format(user_name))
                    break
            else:
                print("用户未注册 or 密码输入错误，请重新登录")
                guan_login()
    else:
        print("用户未注册 or 密码输入错误，请重新登录")
        guan_login()


# 3功能
def tool():


guan_register()
guan_login()
