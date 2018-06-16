# -*- coding:utf-8 -*-
class Robot:
    # 空间换时间
    # 利用python字典　　　key:(x,y)  value:count

    def countWaysDP(self, m, x, y, count_dict):
        # print("x=", x, "y=", y)
        if x == 0:
            return 1
        if y == 0:
            return 1
        else:
            count_x_1_y = 0
            count_x_y_1 = 0
            if m[x - 1][y] == 1:
                if (x - 1, y) in count_dict.keys():
                    count_x_1_y = count_dict[(x - 1, y)]
                else:
                    count_x_1_y = self.countWaysDP(m, x - 1, y, count_dict) % 1000000007
                    count_dict[(x-1, y)] = count_x_1_y

            if m[x][y - 1] == 1:
                if (x, y - 1) in count_dict.keys():
                    count_x_y_1 = count_dict[(x, y - 1)]
                else:
                    count_x_y_1 = self.countWaysDP(m, x, y - 1, count_dict) % 1000000007
                    count_dict[(x, y-1)] = count_x_y_1

            return (count_x_1_y + count_x_y_1) % 1000000007

    def countWays(self, m, x, y):
        count_dict = {}
        return self.countWaysDP(m, x - 1, y - 1, count_dict) % 1000000007

if __name__=="__main__":
    upstairs = Robot()
    m = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1],
     [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    a = 11
    b = 4
    print(upstairs.countWays(m, a, b))
    # for i in range(20):
    #     print(upstairs.countWays(i, i))