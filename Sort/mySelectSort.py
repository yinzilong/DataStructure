#coding=utf-8

#i从第一个元素开始遍历
#j从第i+1个元素开始遍历，找到后续循环最小的元素，和第i个元素进行交换

def selectSort(list):
    for i in range(len(list)):
        min_value = list[i]
        min_index = i           #用来记录最小的元素的下标
        for j in range(i+1, len(list)): #找到数组后续元素中最小的元素
            if list[j]< min_value:
                min_value = list[j]
                min_index = j

        #进行元素交换
        temp = list[i]
        list[i] = min_value
        list[min_index] = temp
    return list

if __name__=="__main__":
    R = [49, 38, 65, 97, 76, 13, 27]
    R = selectSort(R)
    print(R)