#coding=utf-8

"""
    中序遍历，非递归
"""
class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree_stack = []
def insert_stack(root):
    while root is not None:
        tree_stack.append(root)
        root = root.left

#中序遍历（左根右）
"""
大致思想：
    1.从根节点开始遍历，若根节点为空，则返回None
    2.否则，若该节点的左子节点不为空，则存进栈，然后继续遍历该节点的左子节点，直到遇到一个没有左子节点的节点(最左边的节点)
    3.然后取出栈顶节点，输出该栈顶节点的值，若该节点有右子节点，则将该出栈节点的右子节点入栈，对这个节点，依然进行第二步的判断
    4.直到栈为空
"""
def mid_order(root):
    if root is None:
        return None
    insert_stack(root)
    #此时最左边的节点都已经入栈
    while len(tree_stack) != 0:
        node_pop = tree_stack.pop()
        print(node_pop.data, end=" ")
        if node_pop.right is not None:
            insert_stack(node_pop.right)

if __name__=="__main__":
    tree = node("D", node("B", node("A"), node("C")), right=node("F", node("E"), node("G")))

    print("\n中序遍历\n")
    mid_order(tree)
