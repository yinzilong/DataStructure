# -*- coding:utf-8 -*-
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# 广度优先搜索
# 依照题意：路径可以是a->b,可以是b->a
class Path:
    def checkPath(self, a, b):
        self.check(a, b)
        self.check(b, a)
        return False

    def check(self, nodeA, nodeB):
        visited = []  # 记录被访问过的结点

        def dfs(nodeA):
            for n in nodeA.neighbors:
                if n == nodeB:
                    return True
                if n not in visited:
                    visited.append(n)
                    dfs(n)

        if nodeA:
            visited.append(nodeA)
            dfs(nodeA)

p = Path()
{[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],[1,2,3,4,5,6],[2,3,4],[3,4,5],[4,5,6,7,8],[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],[6,7,8,9,10],[7,8,9,10,11,12,13],[8,9,10,11,12],[9,10,11,12,13,14,15,16,17,18,19,20,21],[10,11,12,13],[11,12],[12,13,14,15,16,17,18,19,20,21,22],[13,14,15,16,17,18],[14,15,16],[15,16,17,18,19],[16,17,18],[17,18,19,20,21,22,23],[18,19,20,21,22,23,24],[19,20,21],[20,21,22,23,24],[21,22,23,24],[22,23,24],[23,24],[24]}\
    ,[9,2,0,1,1,10,0,2,2,3,0,0,1,3,0,0,1,3,5,0,3,1,0,0,0],16,15


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
        if self.check(a, b) or self.check(b, a):
            return True
        else:
            return False

    def check(self, nodeA, nodeB):
        visited = []  # 记录被访问过的结点

        def dfs(nodeA):
            visited.append(nodeA)
            for n in nodeA.neighbors:
                if n == nodeB:
                    return True
                if n not in visited:
                    dfs(n)

        if nodeA:
            dfs(nodeA)
