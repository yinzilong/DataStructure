#coding=utf-8
"""
真是个神奇的算法：
    把字符串Ａ转成字符串Ｂ
    字符串编辑距离：　插入操作(1)，删除操作(1)，替换操作(2)
    edit[i][j]:　表示A串和B串的编辑距离，表示Ａ串从第0个字符开始到第i个字符和Ｂ串从第0个字符开始到第j个字符，这两个子串的编辑距离
因此，可以推导出：
    edit[i][j]:
        min
        {
            字符串Ａ删除字符A[i]，　　edit[i-1][j] + 1         (只需要比较A[:i-1]和B[:j])
            给字符串Ａ添加字符B[j]   edit[i][j-1] + 1         (只需要比较A[:i]和B[:j-1],因为第j个字符已经相等)
            将A[i]修改为B[j]       edit[i-1][j-1] + flag    (只需要比较A[:i-1]和B[:j-1],加上修改A[i]和B[j]需要的操作)
        }

    i==0 或 j==0　时单独考虑
"""

def edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    edit = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(0, len(str1)+1):
        for j in range(0, len(str2)+1):
            if i == 0 or j == 0:
                if i == 0:
                    edit[i][j] = j
                if j == 0:
                    edit[i][j] = i
            else:
                flag_distance = 1      #潜意识里觉得这里应该是２才对
                if str1[i-1] == str2[j-1]:
                    flag_distance = 0
                edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1, edit[i-1][j-1]+flag_distance)
    return edit

if __name__=="__main__":
    str1 = "cafe"
    str2 = "coffee"
    edit = edit_distance(str1, str2)
    for i in range(0, len(str1)+1):
        for j in range(0, len(str2)+1):
            print(edit[i][j], end=" ")
        print("")
    print("最小编辑距离为：", edit_distance(str1, str2)[len(str1)][len(str2)])

