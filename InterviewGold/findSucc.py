# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left =left
        self.right = right


# 检查变量名，尤其是list
# 检查类的函数的调用有没有加self

class Successor:
    # 既然结点没有重复值，那直接中序遍历，存进list，然后匹配，输出下一个结点不就可以了吗
    def mid_Order(self, root, myList):
        if root is None:
            return
        self.mid_Order(root.left, myList)
        myList.append(root.val)
        self.mid_Order(root.right, myList)

    def findSucc(self, root, p):
        # write code here
        myList = []
        self.mid_Order(root, myList)
        for i in range(len(myList)):
            if myList[i] == p:
                return myList[i + 1]

if __name__=="__main__":
    treeLevel = Successor()
    tree = TreeNode("D", TreeNode("B", TreeNode("A"), TreeNode("C")), TreeNode("F", TreeNode("E"), TreeNode("G")))
    myBool = treeLevel.findSucc(tree, "F")
    print(myBool)