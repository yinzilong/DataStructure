#coding=utf-8

import math
n=3
m=10

values = [11, 22, 30]

"""
三重循环：
    第一重：最后的整数球和
    第二重：外循环ｉ遍历每一个元素
    第三重：内循环j遍历每一个i之后的元素　　进行向下取整
"""

sum_int = 0
for i in range(n):
    for j in range(i+1, n):
        float_i = values[i] * 1.0
        float_j = values[j] * 1.0
        floor_int = int(math.floor(abs(float_i/m-float_j/m)))
        sum_int += floor_int

print(sum_int)
