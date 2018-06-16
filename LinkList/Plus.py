# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class mySingleLinkedList():
    def __init__(self):
        self.head = None   #初始化链表为空表
        self.size = 0

    def getHead(self):
        return self.head

    #检测链表是否为空
    def isEmpty(self):
        return self.head == None

    #在链表前端添加元素
    def add(self, item):
        temp = ListNode(item)
        temp.next = self.head
        self.head = temp

    #在链表尾部添加元素
    def append(self, item):
        temp = ListNode(item)
        if self.isEmpty():
            self.head = ListNode(item)
        else:
            current = self.head
            while  current.next!=None:
                current = current.next #遍历链表
            current.next=temp

    #search检索元素是否在链表中
    def search(self, item):
        current = self.head
        founditem = False
        while current!=None and not founditem:
            if current.val == item:
                founditem = True
            else:
                current = current.next
        return founditem

    #index索引元素在链表中的位置
    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.val == item:
                found = True
            else:
                current = current.next
        if found:
            return count
        else:
            return -1

    #移除队列中某项元素
    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.item == item:
                if not pre:
                    self._head = current.next
                else:
                    pre.setNext(current.next)
                break
            else:
                pre = current
                current = current.next


class Plus:
    def buildLink(self):
        head = mySingleLinkedList()
        for i in range(10, 0, -1):
            head.append(i)
        return head

    def buildLink(self, num_list):
        head = mySingleLinkedList()
        for i in num_list:
            head.append(i)
        return head


    def printLink(self, head):
        node = head
        while (node != None):
            print(str(node.val) + "->", end="")
            node = node.next

    # 注意累加的进位
    # 两个整数可能位数不一样
    # 将结果存进一个新链表，再利用数位的累乘计算出来
    def plusAB(self, a, b):
        # 当两个链表都不为空时
        # 当用来存储进位的a链表为空时，可以判断b链表是否已空，也空，就新建结点。不过也可以考虑直接存放在新的链表结点
        aNode = a
        bNode = b
        newHead = ListNode(0)
        newNode = newHead

        while (aNode is not None and bNode is not None):
            if ((aNode.val + bNode.val + newNode.val) >= 10):
                addValue = 1
                remainValue = aNode.val + bNode.val + newNode.val - 10
            else:
                addValue = 0
                remainValue = aNode.val + bNode.val + newNode.val
            newNode.val = remainValue
            # 结点后移
            newNode.next = ListNode(addValue)
            newNode = newNode.next
            aNode = aNode.next
            bNode = bNode.next

        # a链表不为空，考虑 和链表和a链表之和
        while (aNode is not None):
            if newNode.val + aNode.val == 10:
                newNode.val = 0
                newNode.next = ListNode(1)
                newNode = newNode.next
                aNode = aNode.next
            else:
                newNode.val = newNode.val + aNode.val
                newNode.next = aNode.next
                break
        # b链表不为空
        while (bNode is not None):
            if newNode.val + bNode.val == 10:
                newNode.val = 0
                newNode.next = ListNode(1)
                newNode = newNode.next
                bNode = bNode.next
            else:
                newNode.val = newNode.val + bNode.val
                newNode.next = bNode.next
                break
        return newHead

p = Plus()
singledLinkA = p.buildLink([7, 4, 0, 7, 5])
singledLinkB = p.buildLink([2, 7, 2, 3, 4])
p.printLink(p.plusAB(singledLinkA.getHead(), singledLinkB.getHead()))