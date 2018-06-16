#coding=utf-8
import sys


def findKth( k):
    num = {}
    pos2 =0
    pos3 =0
    pos5 =0
    num[0] = 1
    for i in range(1, k+1):
        num[i] = min(num[pos2]*2, min(num[pos3]*3, num[pos5]*5) )
        if (num[i] == num[pos2]*2):
            pos2+=1
        if (num[i] == num[pos3]*3):
            pos3+=1
        if (num[i] == num[pos5] * 5):
            pos5 += 1
    return num[k]


for line in sys.stdin:
    a = line.split()
    k = int(a[0])
    print(k)
    res = findKth(k-1)
    print(res)

