#coding=utf-8

#两个部分组成：
#递归算法主体（包括递归结束条件和　以中点分割左右两边分别排序再合并）
#合并两个数组

#递归结束条件：数组的长度<=1
#合并算法：


def merge(a,b):
    c =[]
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    #·拼接第二个
    if i == len(a):
        c.extend(b[j:])
    #拼接第一个
    if j == len(b):
        c.extend(a[i:])
    return c                #记得一定要返回排序完后的数组

#递归算法太牛逼啦
def myMergeSort(list):
    if len(list)<=1:
        return list
    middle = len(list)//2
    left = myMergeSort(list[:middle])
    right = myMergeSort(list[middle:])
    return merge(left, right)

if __name__ == "__main__":
    if __name__ == "__main__":
        R = [4, 7, 8, 3, 5, 9]
        R = myMergeSort(R)
        print(R)
