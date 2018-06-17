#coding=utf-8
import sys
import copy


def count_lessZero(list_int):
    count=0
    for num in list_int:
        if num<=0:
            count +=1
    return count

if __name__ == "__main__":
    # 读取第一行的n，表示数组长度
    n = 10
    values = [15, 0, 0, 0, 0, 20, 0, 0, 0, 30]
    max_list = []
    for i in range(n):
        each_list = []
        for j in range(i, n):
            each_list.append(values[j])
            if (sum(each_list)>sum(max_list) and count_lessZero(each_list)<=3):
                max_list = copy.deepcopy(each_list)
    print(sum(max_list))
