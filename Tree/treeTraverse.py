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
    print(tree.data, end=" ")
    pre_order(tree.left)
    pre_order(tree.right)

#中序遍历（左根右）
def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print(tree.data, end=" ")
    mid_order(tree.right)

#后序遍历（左右根）
def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data, end=" ")

#层次遍历（其实就是广度优先搜索） 后期(借助一个队列就可以)
def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue)>0:
        queue_head = queue.pop(0)
        print(queue_head.data, end=" ")
        if queue_head.left is not None:
            queue.append(queue_head.left)
        if queue_head.right is not None:
            queue.append(queue_head.right)

#求二叉树的叶子节点个数（某节点的叶子节点的个数等于左子树叶子数目和右子树叶子节点数目之和）
def get_leaf_num(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return get_leaf_num(root.left) + get_leaf_num(root.right)


#递归建立一棵平衡二叉树
"""
主要思想：
    以二分查找的形式建树
    mid的值用来形成根节点
    [:mid]用来形成左子树
    [mid+1:]用来形成右子树
"""
def build_tree(num_list):
    left = 0
    right = len(num_list)-1
    if left > right:
        return None
    mid = (left + right)//2
    root = node(num_list[mid])
    root.left = build_tree(num_list[:mid])
    root.right = build_tree(num_list[mid+1:])
    return root

#求树的深度
def depth(tree):
    if tree is None:
        return 0        #深度是一个整数，需要比较大小，所以09要返回0，而不能是None
    return max(depth(tree.left), depth(tree.right))+1

#交换根节点的左右儿子（从根节点开始，递归的交换左右节点的值）
def swap_left_right(root):
    if root is None:
        return
    #交换左右子节点
    temp = root.left
    root.left = root.right
    root.right = temp

    swap_left_right(root.left)
    swap_left_right(root.right)
    return root

#判断二叉树中是否含有某个数字
def contain_num(root, num):
    if root is None:
        return False
    if root.data == num:
        return True
    if(contain_num(root.left, num)):
        return True
    return contain_num(root.right, num)

#找两个节点的最近公共祖先
"""
　如果根节点和任意一个匹配，那么根节点就是最近公共祖先
　否则：
    如果node1和node2分别在root的左右子树中，那么root就是最近公共祖先
    如果node1和node2都在root的左子树中，即root.right==null，那么就在root.left中找
    如果node1和node2都在root的右子树中，即root.left==null，那么就在root.right中找
"""
def common_parent_node(root, node1, node2):
    if root==None or node1==None or node2==None:
        return None
    if root==node1 or root==node2:
        return root
    left_root = common_parent_node(root.left, node1, node2)
    right_root = common_parent_node(root.right, node1, node2)
    if left_root and right_root:   #最终都是要通过这一步拿到真正的答案，其余的两个都是调用下函数
        return root
    if left_root is None:
        return right_root
    if right_root is None:
        return left_root

#路径上的节点的值的和为某一数值的所有路径（以叶子节点结束）
"""
定义两个数组pathArray, onePath, pathArray用于存储所有符合条件的路径，onePath用于存储当前遍历的路径
－类似深度优先搜索，每遍历到一个节点，就将其加入到onePath中，并判定是否符合其他条件
1.为叶子节点且和等于要求的整数，则将数组存储至pathArray中，并换其他路径继续搜寻
2.和小于要求的整数，则向当前节点的左右子树依次深度优先搜索
3.和大于要求的整数，则直接换路搜索
"""
onePath = []
pathArray = []
def find_allPath_common_value(root, num):
    if root is None:
        return pathArray
    onePath.append(root.data)
    num = num - root.data
    if num == 0 and root.left is None and root.right is None:
        pathArray.append(onePath[:])
    elif num > 0:
        find_allPath_common_value(root.left, num)
        find_allPath_common_value(root.right, num)
    onePath.pop()
    return pathArray



if __name__=="__main__":
    tree = node("D", node("B", node("A"), node("C")), right=node("F", node("E"), node("G")))

    print("\n前序遍历")
    pre_order(tree)

    print("\n\n中序遍历")
    mid_order(tree)

    print("\n\n后序遍历")
    post_order(tree)

    print("\n\n层次遍历")
    level_order(tree)

    print("\n\n树的深度")
    print(depth(tree))

    my_tree = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("\n新建立的树的层次遍历")
    level_order(my_tree)

    print("\n\n树的叶子节点的个数：")
    print(get_leaf_num(my_tree))

    print("\n\n交换树的左右孩子节点,然后层次遍历输出：")
    print(level_order(swap_left_right(tree)))    #这里有一个多余的输出

    print("\n\n判断二叉树中是否有某个值：")
    print(contain_num(my_tree, 8))

    print("\n\n寻找两个节点的公共祖先：")
    print(common_parent_node(my_tree, my_tree.left.left, my_tree.left.right).data)

    print("\n\n和为某一值的所有路径：")
    print(find_allPath_common_value(my_tree, 14))