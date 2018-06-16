# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class TreeLevel:
    #先序遍历
    #根左右
    #每次root指向子节点时，深度减１，当深度为０时，将所有的元素放入链表
    def firstTraverse(self, root, dep, node_list):
        if root is None:    #递归终止条件
            return
        if dep == 0:
            node_list.append(root.val)
        self.firstTraverse(root.left, dep-1, node_list)
        self.firstTraverse(root.right, dep-1, node_list)


    def getTreeLevel(self, root, dep):
        node_list = []
        self.firstTraverse(root, dep, node_list)
        #拿到结点list，拼接成链表
        head = ListNode(node_list[0])
        endNode = head
        for node in node_list[1:]:
            newNode = ListNode(node)
            endNode.next = newNode
            endNode = newNode
        return head


if __name__=="__main__":
    treeLevel = TreeLevel()
    tree = TreeNode("D", TreeNode("B", TreeNode("A"), TreeNode("C")), TreeNode("F", TreeNode("E"), TreeNode("G")))
    head = treeLevel.getTreeLevel(tree, 2)
    node = head
    while node is not None:
        print(node.val)
        node=node.next