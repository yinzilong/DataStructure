#coding=utf-8

#冒泡排序的结束标志，一次冒泡中没有发生元素交换，表示已经全部按照从小到大排列
#首先设计循环次数i从n到2
#循环每一个元素j,从0一直比较到i
#借助一个空间temp
#每次排序好一个元素

"""
i为什么从n->1?
    因为每一次冒泡可以排列好一个元素，所以后面的肯定不用再排序了
注意需要一个flag,记录每次是否会交换元素
"""
def bubbleSort(list):
    flag = False    #若一轮过后没有元素交换，表示已经排序完毕
    for i in range(len(list)-1, 1, -1): #这里的i的范围是len(list)-1 到 1,因为python的函数只遍历到尾标+1,即2(len(list)-1就是数组的最后一个元素)
        #print(i)
        for j in range(0, i):
            if list[j] > list[j+1]:
                flag = True             #发生了元素交换
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        if flag is False:
            return list
    return list


if __name__=="__main__":
    R = [49, 38, 65, 97, 76, 13, 27]
    R = bubbleSort(R)
    print(R)