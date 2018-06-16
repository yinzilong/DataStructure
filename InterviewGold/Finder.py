# -*- coding:utf-8 -*-

class Finder:
    #二分查找法，只是要修改判断条件
    #a[mid]>x,本来要在右边找，但是如果x>a[right], 并且a[mid]<a[left]，则在左边找
    #a[mid]<x,本来要在左边找，但是如果x<a[left],并且a[mid]>a[right],则在右边找
    def findElement(self, A, n, x):
        left = 0
        right = len(A)-1
        while left <= right:
            mid = (left + right)//2
            if A[mid] == x:
                return mid
            else:
                if x>A[mid]:                 #本来应该找右边
                    if x>A[right] and A[mid]<A[left]:
                        right = mid-1        #找左边
                    else:
                        left = mid +1        #找右边
                elif x < A[mid]:             #本来应该找左边
                    if x<A[left] and A[mid]>A[right]:
                        left = mid +1        #找右边
                    else:
                        right = mid -1        #找左边
if __name__=="__main__":
    find = Finder()
    A = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,1,2,3,4,5,6,7,8,9]
    n = 80
    x = 6
    print(find.findElement(A, n, x))