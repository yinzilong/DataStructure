# -*- coding:utf-8 -*-

class myStack:
    # 先按照身高排序，在按照体重来进行动态规划
    # 按体重进行排序，再按照身高来进行动态规划
    # 返回值大的一个
    # 看来只需要按照升高排序就够了，不然还交换每个子列表的元素，再进行排序
    def getGoodNum(self, lists, n):
        longest = {}
        longest[0] = 1
        for i in range(1, len(lists)):
            maxlen = -1
            for j in range(0, i):   #找到之前出现过的自己满足的，最长的递增子序列长度
                if(lists[i][1] > lists[j][1] and maxlen < longest[j]):
                    maxlen = longest[j]
            if maxlen >= 1:
                longest[i] = maxlen + 1
            else:
                longest[i] = 1
        return max(longest.values())

    def getHeight(self, actors, n):
        myActors = sorted(actors)
        return self.getGoodNum(myActors, n)

if __name__=="__main__":
    find = myStack()
    list = [[1,2],[3,4],[5,6],[7,8]]
    length = 4
    print(find.getHeight(list, length))