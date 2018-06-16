#coding=utf-8

#犯错：别把函数写在了别的类里面，在参数中会有self的区别
class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#前序遍历（根左右）
def pre_order(tree):
    if tree is None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

#中序遍历（左根右）
def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print(tree.data)
    mid_order(tree.right)

#后序遍历（左右根）
def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)

#求树的深度
def depth(tree):
    if tree is None:
        return 0        #深度是一个整数，需要比较大小，所以要返回0，而不能是None
    return max(depth(tree.left), depth(tree.right))+1



#层次遍历（） 后期(先摸清思想)


if __name__=="__main__":
    tree = node("D", node("B", node("A"), node("C")), right=node("F", node("E"), node("G")))

    print("\n前序遍历\n")
    pre_order(tree)

    print("\n中序遍历\n")
    mid_order(tree)

    print("\n后序遍历\n")
    post_order(tree)

    print("\n树的深度\n")
    print(depth(tree))