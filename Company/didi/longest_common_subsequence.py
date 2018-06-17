#coding=utf-8

"""
最长公共子序列:
    子串要求字符必须是连续的，但是子序列不一样．
    最长公共子序列是一个十分实用的问题，它可以描述两段文字之间的相似度，即它们的雷同程度，从而可以辨别抄袭
解法：动态规划的思想
    一个矩阵记录两个字符串的中匹配情况，若是匹配则为左上方的值加１，否则为左方和上方的最大值．
    一个矩阵记录转移方向，然后根据转移方向，回溯找到最长子序列
从左下到右上：
    若s1[i]==s2[j],则m[i][j] = m[i-1][j-1] + 1
    否则：m[i][j] = max(m[i-1][j],m[i][j-1])的最大值
    不过要记录好转移的方向
    因为是动态规划，所以在计算m[i][j]之前，m[i-1][j-1]和m[i-1][j]，m[i][j-1]肯定都已经知道了
"""

def getLongestCommonSubSequence(str1, str2):
    dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    directions = [[None for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if str1[i]==str2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                directions[i+1][j+1] = "ok"
            elif dp[i+1][j] > dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
                directions[i+1][j+1] = "left"
            else:
                dp[i+1][j+1] = dp[i][j+1]
                directions[i+1][j+1] = "down"
    print(dp[i+1][j+1])
    #遍历打印出路径(如果是"ok"，才进行输出，其他情况改变遍历的下标即可)
    i = len(str1)
    j = len(str2)
    result_subsequence = ""
    while(i>0 and j>0):
        if directions[i][j]=="ok":
            result_subsequence = result_subsequence + str1[i-1]
            i = i-1
            j = j-1
        else:
            if directions[i][j] == "left":
                i = i-1
            elif directions[i][j] == "down":
                j = j-1
    return dp[len(str1)][len(str2)], result_subsequence[::-1]

if __name__=="__main__":
    str1 = "ABCBDAB"
    str2 = "BDCABA"

    num, subString = getLongestCommonSubSequence(str1, str2)
    print("最长连续子串的最大长度： ", num)
    print("最长连续子串为： ", subString)