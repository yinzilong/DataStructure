#coding=utf-8

"""
    数组arr[], 表示各种面值的货币，例如[1,2,3,5]
    aim=20  表示要找的钱数
    求组成aim需要的最少货币数
    dp[i][j]: 使用前i种货币来组成j元
    dp[i-1][j]: 不使用当前货币，仅使用前i-1中货币来组成j元
    dp[i][j-arr[i]]＋１：只使用一张当前货币情况下来组成j-arr[i]元

    从左上到右下：
        每当计算dp[i][j]时：
            dp[i-1][j],dp[i-2][j],dp[i-3][j],...,都已经知道
            dp[i][j-1],dp[i][j-2],dp[i][j-3],...,都已经知道
    特殊情况：
        dp[*][0]=0
        dp[0][*]=INT_MAX
    记得横纵坐标的零下标都舍弃不用
"""


import sys

def coinChange(arr, aim):
    int_max = sys.maxsize   #整型的最大值
    dp = [[0 for j in range(aim+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(aim+1):
            if i == 0 and j == 0:
                dp[i][j] = 0
            else:
                if i == 0:
                    dp[i][j] = int_max
                if j == 0:
                    dp[i][j] = 0
                if i > 0 and j > 0:
                    if j-arr[i-1] < 0:
                        dp[i][j] = dp[i-1][j]   #此时无法使用面值为arr[i]的纸币
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i-1]]+1)

    #打印
    for i in range(len(arr)+1):
        for j in range(aim+1):
            print(dp[i][j], end=" ")
        print("")

if __name__=="__main__":
    coinChange([25, 21, 10, 5, 1], 63)





