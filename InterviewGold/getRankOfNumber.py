# -*- coding:utf-8 -*-

# 二叉查找树：结点的左子树的元素一定小于等于本身，结点右子树的元素一定大于等于本身
class RankNode:
    def __init__(self, data=None):  # 给data指定了一个默认构造函数
        self.left = None
        self.right = None
        self.data = data  # 该节点的元素值
        self.left_size = 0  # 该节点的秩，即左边的结点的数量

    def insert(self, num):
        if num <= self.data:
            if self.left != None:
                self.left.insert(num)
            else:
                newNode = RankNode(num)
                self.left = newNode
            self.left_size += 1         #竟然死在了这句代码里面，把+1语句写进了else分支
        else:
            if self.right != None:
                self.right.insert(num)
            else:
                newNode = RankNode(num)
                self.right = newNode

    def getRank(self, num):

        if num == self.data:
            return self.left_size
        elif num < self.data:
            return self.left.getRank(num)
        else:
            return self.left_size + 1 + self.right.getRank(num) #这里的递归要注意，还不熟悉递归



class Rank:

    # 高效的数据结构：二叉查找树
    # 算法：查找，排序
    # 建立一个RankNode类
    # 每次来了新节点，首先进行插入操作，然后进行取秩操作
    def getRankOfNumber(self, A, n):
        res_list = []
        root = None
        #插入操作
        for i in range(len(A)):
            if root is None:
                root = RankNode(A[i])
                res_list.append(0)
            else:
                root.insert(A[i])
                res_list.append(root.getRank(A[i]))
        return res_list

if __name__=="__main__":
    rank = Rank()
    input_list = [1478872,2239674,1441267,2527575,2056092,2788049,2810239,2276038,2517691,950366,809051,801761,2682907,1286004,1275053,683268,1840468,992943,3004624,1217244,2568919,136333,294932,597040,2811419,1161358,983756,1765868,648621,2570299,1929301,642767,1904827,2507236,2866636,552255,1069129,1695656,931968,513233,3008982,2180130,2182736,698771,2196006,744352,2746614,1900145,1219192,2145908,1598445,1459451,1580620,44,2333175,1485733,1666273,1640796,1355392,1035140,1834066,2560806,366129,3008956,2625119,654811,1444028,113541,1899483,1186194,1213252,138451,1608744,1194924,2723466,509130,896587,796812,1219817,1754118,2430381,781824,2177158,2866775,1962617,765778,2522305,1876603,669406,1929973,928956,1714732,304638,1989582,2708067,1978152,1572745,507466,2384842,1415165,511151,2215090,875516,1929421,1837224,219661,2954007,1670655,874477,210961,2761875,2519108,1269212,604896,1069890,994782,2880938,384869,567612,836963,589137,1437142,1527143,2778956,831471,1821811,2199125,1512751,876532,1936623,702004,2629917,469263,2731257,772307,2120565,2050648,1694991,200241,1960173,2421470,509174,86257,3000507,667548,3026220,271153,1833865,1442870,313318,2574314,2518862,61565,1912768,1970424,2223667,1980876,2773928,1815419,204096,648920,1981501,326197,2192833,787225,2323637,845056,424613,2391722,1260736,1650795,1807609,14476,2185334,339452,2637132,503889,1399057,2246084,1417700,1369043,2877240,2647478,2055993,1972083,2412793,941988,52036,2364924,1423294,421295,1643598,2649722,2430377,1622111,2253994,2133598,2374305,282962,1232267,873885,411631,2685563,2456156,100251,747741,2814669,2275141,257687,2603468,2611997,1497014,1134242,2459536,2532732,355949,2841707,1994341,2320809,592957,1009609,2806427,2863571,732737,2577298,2122902,1147614,1916583,98841,316670,212728,1934188,1987097,122507,2033224,2284374,2577323,3015136,943862,570209,1778286,1242654,2362077,501516,2272515,472453,139619,369023,456791,1760019,101228,2871829,815894,557120,2121611,686168,2790594,1858133,1954139,2719633,785030,2789818,2769176,2850710,11637,2132737,1985714,2568523,1885507,2262306,2009962,2836032,768113,1670789,1877298,2102414,873529,2329519,1150241,2284315,2030951,1815488,1843075,739806,2014424,2242829,409716,14871,2240368,1043712,619401,512738,12883,1940022,2727626,206156,355377,2508846,751754,1112871,827338,523907,1974268,2722638,1297945,1676717,2886232,2011450,915197,590187,1210443,2010930,2857618,602781,1397651,2045257,2194626,226245,813717,1700443,262307,1223019,433432,1787247,1380040,552499,890406,1305577,2794202,1874707,4105,1119307,1763889,1747603,431280,911677,1907898,1742696,779944,368414,2189298,2905077,1320334,1808393]
    num = 344
    print(rank.getRankOfNumber(input_list, num))


