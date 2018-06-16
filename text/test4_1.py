
#coding=utf-8
import sys
import math
if __name__ == "__main__":
    # 读取第一行的n
    # line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = [3, 10]
    n = nums[0]
    m = nums[1]
    ans = [11, 22, 30]
    # for i in range(n):
        # 读取每一行
        #line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        # values = map(int, line.split())
        # for v in values:
        #     ans.append(v)
    #算法
    sum_int = 0
    for i in range(n):
        for j in range(i+1, n):
            float_i = ans[i] * 1.0
            float_j = ans[j] * 1.0
            floor_int = int(math.floor(abs(float_i/m-float_j/m)))
            sum_int += floor_int
print(int(2.8))
