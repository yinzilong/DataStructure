# -*- coding:utf-8 -*-

# 变形的二叉查找树
# 结点的左子树大于等于该节点的值，右子树小于该节点的值
class RankNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
        self.left_size = 0  # 大于当前结点的个数，那就是要构造一个变形的二叉查找树

    def insert(self, d):
        if d >= self.data:
            if self.left is None:
                newNode = RankNode(d)
                self.left = newNode
            else:
                self.left.insert(d)
            self.left_size += 1
        else:
            if self.right is None:
                newNode = RankNode(d)
                self.right = newNode
            else:
                self.right.insert(d)

    def getReversePair(self, num):
        if num == self.data:
            return self.left_size
        elif num >= self.data:
            return self.left.getReversePair(num)
        else:
            return self.left_size + 1 + self.right.getReversePair(num)


class AntiOrder:
    def count(self, A, n):
        res_list = []
        root = None
        for i in range(len(A)):
            if root is None:
                root = RankNode(A[i])
                res_list.append(0)
            else:
                root.insert(A[i])
                res_list.append(root.getReversePair(A[i]))
        return sum(res_list)

if __name__=="__main__":
    rank = AntiOrder()
    input_list = [1,2,3,4,5,6,7,0]
    num = 8
    print(rank.count(input_list, num))