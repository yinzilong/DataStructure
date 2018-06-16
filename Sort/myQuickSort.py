#coding=utf-8

#判断异常
#指定枢纽位置
#制定i,j的值
#快排的主要思路
#递归
#一次快排结束的标志的i=j
#整体结束的标志是传入的参数left>right
def quickSort(R, left, right):
    if left > right:
        return
    temp = R[left]
    i = left
    j = right
    while i<j:
        while i<j and R[j]>temp:
            j -= 1
        if(i<j):                    #此处一定要加判断，不然最后i=j时，i和j还会继续变化
            R[i] = R[j]
            i += 1
        while i<j and R[i]<temp:
            i += 1
        if i<j:
            R[j] = R[i]
            j -= 1
    R[i] = temp

    quickSort(R, left, i-1)
    quickSort(R, i+1, right)
    return R

if __name__=="__main__":
    R = [49, 38, 65, 97, 76, 13, 27]
    R = quickSort(R, 0, len(R)-1)
    print(R)