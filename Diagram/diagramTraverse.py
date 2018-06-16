#coding=utf-8

class Graph(object):
    def __init__(self, *args, **kwargs):
        self.node_neightbors={}         #用来为每一个结点存邻居结点，键值对  node:[]
        self.visited={}                 #用来记录该结点是否已经被访问过     node:bool

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neightbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if(v not in self.node_neightbors[u]) and (u not in self.node_neightbors[v]):
            self.node_neightbors[u].append(v)
            if (u!=v):
                self.node_neightbors[v].append(u)

    def nodes(self):
        return self.node_neightbors.keys()

    # 图的深度遍历
    """
    1.访问指定的起始顶点
    2.若当前访问的顶点的邻接顶点有未被访问的，则任选一个访问之；反之，退回到最近访问过的顶点；直到与起始顶点相同的全部顶点都访问完毕。
    3.若此时还有顶点没有被访问，则再选其中一个顶点作为其实是顶点并访问之，转2；反之，遍历结束
        核心思想部分：
            遍历一个结点node
            首先将该节点的visited设置为True
            然后循环他所有的邻居结点，若没有被遍历过，就对该邻居结点进行深度优先遍历
        记得检查图中是否还有其他结点没有被遍历，因为图分为连通图和非连通图
    """
    def depth_first_search(self, root=None):
        order = []  #用来存储遍历顺序
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for neightbor in self.node_neightbors[node]:
                if neightbor not in self.visited:
                    dfs(neightbor)

        if root:
            dfs(root)

        #看是否还有其他未遍历结点
        for node in self.nodes():
            if node not in self.visited:
                dfs(node)

        print(order)
        return order


    #图的广度遍历（先摸清思想）
    """
        1.访问顶点vi
        2.访问vi所有未被访问的领结点我,w2,...,wk
        3.依次访问从这些邻接点出发，访问他们的所有未被访问的邻接点；以此类推，知道图中所有访问过的顶点的邻接点都被访问
        为实现3.需要保存步骤2中访问的顶点，而且访问的这些顶点的邻接点的顺序为：先保存的顶点，其邻接点先被访问，用到queue
        queue[]保存已经访问的结点
        order[]保存访问的顺序

        直接从队首取结点
        将该结点设置为已访问
        遍历所有邻居结点，若邻居结点没有被访问，且没有进入队列，就进入队列
    """
    def breadth_first_search(self, root=None):
        order = []
        queue = []

        def bfs():
            while(len(queue)>0):
                node = queue.pop(0)     #队首出结点
                order.append(node)
                for n in self.node_neightbors[node]:
                    if n not in self.visited:
                        self.visited[n] = True
                        queue.append(n)

        if root:
            self.visited[root] = True
            queue.append(root)
            bfs()

        for node in self.nodes():
            if node not in self.visited and node not in queue:
                self.visited[node] = True
                queue.append(node)
                order.append(node)
                bfs()
        print(order)
        return order


if __name__=="__main__":
    g = Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge((1,2))
    g.add_edge((1,3))
    g.add_edge((2,4))
    g.add_edge((2,5))
    g.add_edge((4,8))
    g.add_edge((5,8))
    g.add_edge((3,6))
    g.add_edge((3,7))
    g.add_edge((6,7))
    print("nodes:", g.nodes())
    print("广度优先遍历：")
    order = g.breadth_first_search(1)
    # print("深度优先遍历:")
    # order = g.depth_first_search(1)

