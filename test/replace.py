# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# 想把文件里面的关键字和表名全部转成大写
#
# 1、读文件
# 2、定义关键字和表名规范
# 3、将关键字和符合表名规范的字母全部转成大写 lower小 upper大
# """
# import os
#
# # 定义一个关键字列表
# args_world_list = [
#     'select ', 'from ', 'where ', 'group by ', 'having ', 'order by ', 'left join ', ' as ', 'and', 'create ', 'table '
# ]
#
# # def file_read_content_upper()
# file_path = r'D:\cgyi20211025\test\testcgy.txt'
# # with open(file_path, 'r', encoding='UTF-8') as file_path_read_stream:
# #     for file_content_line in file_path_read_stream.readlines():
# #         # file_split = file_content_line.split()
# #         # print(file_split)
# #         # for i in file_split:
# #         #     if i.
# #         for i in args_world_list:  # 遍历关键字集合
# #             for j in file_content_line.split():  # 遍历文件集合
# #                 print("文件前{}".format(file_content_line))
# #                 test = file_content_line.replace(i, i.upper())
# #                 print("文件后{}".format(file_content_line))
# # print(file_content_line)
#
# with open(file_path, 'r', encoding='UTF-8') as file_path_read_stream:
#     file_cont = file_path_read_stream.read()
#     print(file_cont)
#     for args_world in args_world_list:
#         file_cont2 = file_cont.replace(args_world, args_world.upper())
#     print(file_cont2)

import re

search_yesorno = re.compile(r'''yesorno":(.*?),''')
yesorno = search_yesorno.findall('{"list":[{"event":"search-answerv2","tab":"综合","searchId":"67a7ea348ff1fe1ee24e84c56d70f7ed","seq":29,"index":1,"cardId":"answerv2_5647456","cardLevel":"module","type":"audio","yesorno":false,"f_openid":"ooJQ342NFOCjs5BAztFSV6rZJ5IU","f_userid":"ohNH9stWGEZu_pc_1KN4yOtb5J3g","f_channel":"AAGyrAqmWG9aCL220ZMG8IZO","f_cityCode":"430100","f_scene":1019,"f_abtest":"","f_edition":"新首页(1152)-V5.6.3-20210323","trace":null,"wzChannel":"wenyiwen","theme":"blue","query":"拔牙多少钱一颗智齿","abidList":["116.0.48_2","116.0.48_2"],"time":1630476508224},{"event":"search-quick_wenzhen","tab":"综合","searchId":"67a7ea348ff1fe1ee24e84c56d70f7ed","seq":29,"index":2,"cardId":"quick_wenzhen_20215111","cardLevel":"module","f_openid":"ooJQ342NFOCjs5BAztFSV6rZJ5IU","f_userid":"ohNH9stWGEZu_pc_1KN4yOtb5J3g","f_channel":"AAGyrAqmWG9aCL220ZMG8IZO","f_cityCode":"430100","f_scene":1019,"f_abtest":"","f_edition":"新首页(1152)-V5.6.3-20210323","trace":null,"wzChannel":"wenyiwen","theme":"blue","query":"拔牙多少钱一颗智齿","abidList":["116.0.48_2","116.0.48_2"],"time":1630476508225},{"event":"search-merged_doctors","tab":"综合","searchId":"67a7ea348ff1fe1ee24e84c56d70f7ed","seq":29,"index":3,"cardId":"merged_doctors_858634","cardLevel":"module","f_openid":"ooJQ342NFOCjs5BAztFSV6rZJ5IU","f_userid":"ohNH9stWGEZu_pc_1KN4yOtb5J3g","f_channel":"AAGyrAqmWG9aCL220ZMG8IZO","f_cityCode":"430100","f_scene":1019,"f_abtest":"","f_edition":"新首页(1152)-V5.6.3-20210323","trace":null,"wzChannel":"wenyiwen","theme":"blue","query":"拔牙多少钱一颗智齿","abidList":["116.0.48_2","116.0.48_2"],"time":1630476508225},{"event":"search-merged_doctors","tab":"综合","searchId":"67a7ea348ff1fe1ee24e84c56d70f7ed","seq":29,"index":1,"cardId":"merged_doctors_858634","cardLevel":"item","f_openid":"ooJQ342NFOCjs5BAztFSV6rZJ5IU","f_userid":"ohNH9stWGEZu_pc_1KN4yOtb5J3g","f_channel":"AAGyrAqmWG9aCL220ZMG8IZO","f_cityCode":"430100","f_scene":1019,"f_abtest":"","f_edition":"新首页(1152)-V5.6.3-20210323","trace":null,"wzChannel":"wenyiwen","theme":"blue","query":"拔牙多少钱一颗智齿","abidList":["116.0.48_2","116.0.48_2"],"time":1630476508340},{"event":"search-merged_doctors","tab":"综合","searchId":"67a7ea348ff1fe1ee24e84c56d70f7ed","seq":29,"index":2,"cardId":"merged_doctors_858634","cardLevel":"item","f_openid":"ooJQ342NFOCjs5BAztFSV6rZJ5IU","f_userid":"ohNH9stWGEZu_pc_1KN4yOtb5J3g","f_channel":"AAGyrAqmWG9aCL220ZMG8IZO","f_cityCode":"430100","f_scene":1019,"f_abtest":"","f_edition":"新首页(1152)-V5.6.3-20210323","trace":null,"wzChannel":"wenyiwen","theme":"blue","query":"拔牙多少钱一颗智齿","abidList":["116.0.48_2","116.0.48_2"],"time":1630476508340}]}')[0]

print(yesorno)
print(yesorno != 'false')

num = 0
for i in range(555555555555555):
    num+=1
    if i%100000000==0:
        print(i)
print(num)