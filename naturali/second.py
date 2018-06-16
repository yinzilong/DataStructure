#coding=utf-8

#首先对现在的数组array进行排序，然后直接计算第key大的数，用下标取出，就可以
def getKth(array, n, k):
    if k<0 or k>(n*(n-1)//2):
        return None

    list_all = []
    for i in range(len(array)-1):
        for j in range(i, len(array)):
            list_all.append(min(array[i], array[j]))

    #进行排序，从大到小
    sorted(list_all, reverse=True)
    return list_all[k]

if __name__=="__main__":
    print(getKth([5, 3, 4, 2, 1], 5, 8))

