#coding=utf-8


length_list=5
list_int = [15, 0, 0, 0, 20]

def count_lessZero(list_int):
    count=0
    for num in list_int:
        if num<=0:
            count +=1
    return count


max_list = []
for i in range(len(list_int)):
    each_list = []
    for j in range(i, length_list):
        each_list.append(list_int[j])
        if sum(each_list)>sum(max_list):
            max_list = each_list
            print(count_lessZero(each_list))
print(max_list)




