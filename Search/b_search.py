#coding=utf-8

#二分查找法
def bsearch(list, num):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        if list[mid] == num:
            return mid
        if list[mid]>num:
            high = mid-1
        else:
            low = mid+1
    return None

if __name__=="__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(bsearch(list, 8))