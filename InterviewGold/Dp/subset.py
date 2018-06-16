# -*- coding:utf-8 -*-
import copy

class Subset:
    # 返回二维[[],[],[]]

    #假设传进来的ａ是列表的列表
    def buildSubsets(self, A, agolist, n):
        if n==len(A):
            return agolist

        currentList = []
        if n==0:
            currentList.append([A[n]])
        else:

            currentList = copy.deepcopy(agolist)    #深拷贝，浅拷贝的问题
            currentList.append([A[n]])
            for sub in agolist:
                copy_sub = copy.deepcopy(sub)       #深拷贝，浅拷贝的问题
                copy_sub.insert(0, A[n])
                currentList.append(copy_sub)


        return self.buildSubsets(A, currentList, n+1)


    def getSubsets(self, A, n):
        sublist = []      #里面的一个空[]代表空集，之后再删除
        sublist = self.buildSubsets(sorted(A), sublist, 0)
        sublist.reverse()
        return sublist

if __name__=="__main__":
    sub = Subset()
    list = [0,1]
    print(sub.getSubsets(list, 2))
