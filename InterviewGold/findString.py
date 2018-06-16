# -*- coding:utf-8 -*-

class Finder:
    #首先还是取中点mid = (left+right)//2,判断s[mid]是否为空
    #若为空向后移动，要考虑边界问题，这样就可以
    #边界问题只要<=hign，就可以
    #字符串比较,用cmp(),大于返回１，等于返回0，小于返回-1
    def findString(self, s, n, x):
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if s[mid] is "":
                while mid<right and s[mid] is "":
                    mid +=1
            if s[mid] == x:
                return mid
            elif x > s[mid] :
                left = mid +1
            else:
                right = mid -1
        return s[mid]

if __name__=="__main__":
    find = Finder()
    print(find.findString(["","","CFWW","JUNMFCVE","KBVPO","LLQHRIN","P","RDDK","UFEYPGVKFO"],9,"PO"))