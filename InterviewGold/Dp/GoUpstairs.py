# -*- coding:utf-8 -*-

# 这个主要是提高效率的问题，用一个列表进行存储，然后读取即可，和斐波拉切类似
class GoUpstairs:

    def countWaysDP(self, n, way):
        for i in range(4, n + 1):
            way.append(way[0] + way[1] + way[2])
            way.pop(0)
        return way[2]

    def countWays(self, n):
        way = [1, 2, 4]  # 仅仅需要保存前三个数就可以了
        if n <= 0:
            return 0
        if n <= 1:
            return 1
        if n <= 2:
            return 2
        if n <= 3:
            return 4
        else:
            return self.countWaysDP(n, way)//1000000007


if __name__ =="__main__":
    upstairs = GoUpstairs()
    print(upstairs.countWays())
    for i in range(20):
        print(upstairs.countWays(i))