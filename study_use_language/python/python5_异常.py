#!/usr/bin/python
# -*- encoding=utf-8 -*-


# print('第{0}此 结果={1}+{2}'.format(i, result, sum_value(value, num)))


value = int(input("请输入值："))
num = int(input("请输入次数："))
result = 0
for i in range(1, num + 1):
    result_mid = 0
    for j in range(0, i):
        result_mid += value * pow(10, j)  #
    result += result_mid
print(result)
