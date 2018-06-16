# coding=utf-8

"""
    中序遍历，非递归
"""
class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 中序遍历（左根右）
"""
算法思想：
    1.从根节点开始遍历，若根节点为空，则返回None
    2.否则，若该节点的左子节点不为空，则存进栈，然后继续遍历该节点的左子节点，直到遇到一个没有左子节点的节点(最左边的节点)
    3.然后取出栈顶节点，输出该栈顶节点的值，若该节点有右子节点，则将该出栈节点的右子节点入栈，对这个节点，依然进行第二步的判断
    4.直到栈为空
"""
tree_stack_mid = []

def insert_stack_mid(root):
    while root is not None:
        tree_stack_mid.append(root)
        root = root.left

def mid_order(root):
    if root is None:
        return None
    insert_stack_mid(root)
    # 此时最左边的节点都已经入栈
    while len(tree_stack_mid) != 0:
        node_pop = tree_stack_mid.pop()
        print(node_pop.data, end=" ")
        insert_stack_mid(node_pop.right)


# 前序遍历(根左右)
"""
算法思想：
    和中序遍历的主要区别在于：输出根节点的值的时机不一样
    前序遍历时需要在入栈的时候就输出根节点的值
"""
tree_stack_pre = []

def insert_stack_pre(root):
    while root is not None:
        print(root.data, end=" ")
        tree_stack_pre.append(root)
        root = root.left

def pre_order(root):
    if root is None:
        return None
    insert_stack_pre(root)
    while len(tree_stack_pre)!=0:
        node_pop = tree_stack_pre.pop()
        insert_stack_pre(node_pop.right)

#后序遍历（左右根）
"""
算法思想：
    根输出的时机只能是在左右子节点输出之后，所以我得加一个判断条件
    node_traversed = []   #记录已经遍历过的节点
    是否弹出栈顶元素也得加一个条件
"""
tree_stack_post = []
node_traversed = []
def insert_stack_post(root):
    while root is not None:
        tree_stack_post.append(root)
        root = root.left

def post_order(root):
    if root is None:
        return None
    insert_stack_post(root)
    while(len(tree_stack_post)!=0):
        stack_len = len(tree_stack_post)
        node_top = tree_stack_post[len(tree_stack_post)-1] #取栈顶元素
        if node_top.right is not None and node_top.right not in node_traversed:
            node_traversed.append(node_top.right)
            insert_stack_post(node_top.right)
            node_top = tree_stack_post[len(tree_stack_post) - 1]
        if node_top.right is None or node_top.right in node_traversed:
            node_pop = tree_stack_post.pop()
            print(node_pop.data, end=" ")



if __name__ == "__main__":
    tree = node("D", node("B", node("A"), node("C")), right=node("F", node("E"), node("G")))

    print("\n前序遍历\n")
    pre_order(tree)

    print("\n中序遍历\n")
    mid_order(tree)

    print("\n后序遍历\n")
    post_order(tree)

