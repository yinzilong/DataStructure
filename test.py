#coding=utf-8

my_list = [1,22,3,4,4]
your_list = [[1,3],[4,4]]


my_dict ={(1,2):12, (1,3):13}
if (1, 2) in my_dict.keys():
    print("True====")


for i in range(len(my_list)):
    if my_list[i] is not sorted(my_list)[i]:
        print("False")

print(sorted(your_list))

my_list.insert(2, 2333)
print(sorted(my_list, reverse=True))