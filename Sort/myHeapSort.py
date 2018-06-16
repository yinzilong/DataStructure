#coding=utf-8

#堆排序分为三个部分：
#形成大顶堆
#交换函数
#

#构建大顶堆，要求父节点大于孩子节点
#在list[low]到list[high]的范围内，对在low位置上的节点进行调整

#在子堆上进行调整
def sift(list, low, high):
    temp = list[low]
    i = low
    j = 2*i         #左子节点
    while j <high:
        #判断右子节点是否大于左子节点，大于则和右子节点进行交换
        if j+1<high and list[j+1]>list[j]:
            j = j+1
        #如果父节点小于子节点，则进行交换
        if list[j] > temp:
            list[i] = list[j]
            i = j
            j = 2*i
        else:
            break
    list[i] = temp      #为最后确定下来的ｉ节点的赋值
    return list

def heapSort(list):
    num = len(list)//2        #第一个非叶子结点

    #形成大顶堆
    for i in range(num, 0, -1): #是否可以将数据存在下标为0的位置，不可以，否则2*i就等于0，无法求子结点
        sift(list, i, len(list))

    #最顶端元素和最后一个元素进行交换，然后在进行堆的调整，可以用一个列表进行存储，再返回该列表
    for n in range(len(list)-1, 0, -1):
        temp = list[1]
        list[1] = list[n]
        list[n] = temp
        sift(list, 1, n)
    #当循环完毕之后，那么所有的元素已经是从大到小排列
    return list

if __name__=="__main__":
    R = [0, 49, 38, 65, 97, 76, 13, 27, 108]     #从下标为１开始算,0下标处不存储数据
    R = heapSort(R)
    print(R[1:])



