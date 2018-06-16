# -*- coding:utf-8 -*-
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# 广度优先搜索
# 依照题意：路径可以是a->b,可以是b->a
class Path:
    def checkPath(self, a, b):

        if a is None or b is None:
            return False
        if a is b:
            return True

        # if self.check(a, b)  or self.check(b, a):
        #    return True

        s = {}
        if self.judge(a, b, s) or self.judge(b, a, s):
            return True
        else:
            return False

            # 递归 深度优先遍历

    def judge(self, start, end, s):
        for i in start.neighbors:
            if i == end:
                return True
            if id(i) not in s:
                s[id(i)] = 1
                return self.judge(i, end, s)
        return False


    def check(self, nodeA, nodeB, visited):

        for n in nodeA.neighbors:
            if n == nodeB:
                return True
            if n not in visited:
                visited.append(n)
                return self.check(n, nodeB, visited)        #此处的开始结点nodeA,要改成n,困了一个小时！！！！
