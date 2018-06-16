#coding=utf-8

#结束条件，遍历到最后一个元素截止
#两重循环
#外部循环遍历每一个元素
#内部循环是一次与前面已经排序过的元素进行比较
def insertSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1     #这里必须要取j=i-1
        while j>=0 and temp<list[j]:        #一定要注意比较时的变量，是temp而不是list[i],list[i]会变化
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp
    return list

if __name__=="__main__":
    R = [49, 38, 65, 97, 76, 13, 27]
    R = insertSort(R)
    print(R)

#插入排序教我做人