#coding=utf-8


#解释算法的复杂度
#仅需要遍历一次链表，算法的复杂度为O(n)
#去掉末尾
def combine(a, b):
    if a is None:
        return b
    if b is None:
        return a
    listA = list(a)
    listB = list(b)
    while len(listA)>0 and len(listB)>0:
        if listA[len(listA)-1] == listB[0]:
            listA.pop(len(listA)-1)
            listB.pop(0)
        else:
            break
    listA.extend(listB)     #合并list
    return "".join(listA)

if __name__=="__main__":
    print(combine("abcdef", "fedha"))
