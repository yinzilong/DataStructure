# -*- coding:utf-8 -*-
class Robot:
    def countWaysDP(self, x, y):
        if x == 0:
            return 1
        if y == 0:
            return 1
        else:
            return self.countWaysDP(x - 1, y) + self.countWaysDP(x, y - 1)

    def countWays(self, x, y):
        return  self.countWaysDP(x-1, y-1)

if __name__=="__main__":
    upstairs = Robot()
    print(upstairs.countWays(2, 2))
    # for i in range(20):
    #     print(upstairs.countWays(i, i))