# -*- coding:utf-8 -*-
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class MinimalBST:
    def buildMinimalBST2(self, vals, left, right):
        if (left > right):  # 递归终止条件
            return None
        # 取得数组的中间值
        mid = (left + right) // 2
        # 将中间值建立根节点
        root = Node(vals[mid])
        # 左半部形成左子树
        root.left = self.buildMinimalBST2(vals, left, mid - 1)
        # 右半部形成右子树
        root.right = self.buildMinimalBST2(vals, mid + 1, right)
        return root

    def getHeight(self, root):
        if root is None:  # 递归终止条件
            return 0
        return max(self.getHeight(root.left) + 1, self.getHeight(root.right) + 1)

    def buildMinimalBST(self, vals):
        left = 0
        right = len(vals) - 1
        root = self.buildMinimalBST2(vals, left, right)
        return self.getHeight(root)

if __name__=="__main__":
    vals = [1,2,3,4,5,6,7,8,9]
    my = MinimalBST()
    print(my.buildMinimalBST(vals))