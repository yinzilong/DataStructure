# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = left

class Checker:
    # 中序遍历这棵树，看看是否严格递增
    # 排序后的列表和原来的列表比较看是否相同

    def mid_Order(self, root, myList):
        if root is None:
            return
        self.mid_Order(root.left, myList)
        myList.append(root.val)             #这里是收录结点的值，不是结点本身！！！！
        self.mid_Order(root.right, myList)

    def checkBST(self, root):
        myList = []
        self.mid_Order(root, myList)
        # 判断排序后的元素和未排序的元素是否一致
        for i in range(len(myList)):
            if myList[i] is not sorted(myList)[i]:
                return False
        return True

if __name__=="__main__":
    treeLevel = Checker()
    tree = TreeNode("D", TreeNode("B", TreeNode("A"), TreeNode("C")), TreeNode("F", TreeNode("E"), TreeNode("G")))
    myBool = treeLevel.checkBST(tree)
    print(myBool)
