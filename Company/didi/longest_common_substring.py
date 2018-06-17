#coding=utf-8

"""
最长公共子字符串：
    动态转移方程：
        如果xi==yj:   c[i][j]=c[i-1][j-1]+1
        如果xi!=yi:   c[i][j]==0
    最后，最长子串的长度：
        max{c[i][j], 1<=i<=n, 1<=j<=m}
"""
#声明二维数组也要注意，用列表生成式
def getLongestCommonSubstring(str1, str2):
    c = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]   #内循环i表示列，外循环j表示行,为了方便计算，必字符串长度多了一列
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = 0
    max_num = c[0][0]
    max_str1_endIndex = 0
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if c[i][j] > max_num:
                max_num = c[i][j]
                max_str1_endIndex = i
    return max_num, str1[max_str1_endIndex-max_num:max_str1_endIndex]

if __name__=="__main__":
    str1 = "abcdefghijklmnopwa"
    str2 = "abcsafjklmnopqrstuvw"

    num, subString = getLongestCommonSubstring(str1, str2)
    print("最长连续子串的最大长度： ", num)
    print("最长连续子串为： ", subString)


