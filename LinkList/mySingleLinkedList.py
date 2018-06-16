#coding=utf-8
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



# 重点：保持原来的顺序不变
# 利用两个链表，一个用来存储比x小的元素，一个用来存储比x大的元素
# 利用头结点新建两个链表，后续需要删除头结点，因为python目前还不好用ListNode
# 遍历原始链表，进行元素的分配
# 分配完后，判断第二个链表是否为空，进行元素的拼接
class Partition:

    def buildLink(self):
        head = mySingleLinkedList()
        for i in range(10, 0, -1):
            head.append(i)
        return head

    def printLink(self, head):
        node = head
        while (node != None):
            print(str(node.val) + "->", end="")
            node = node.next

    def partition(self, pHead, x):
        smallNodeHead = ListNode(pHead.val)
        smallNodeEnd = smallNodeHead

        biggerNodeHead = ListNode(pHead.val)
        biggerNodeEnd = biggerNodeHead

        node = pHead.next
        while (node is not None):
            if node.val < x:
                newNode = ListNode(node.val)
                smallNodeEnd.next = newNode
                smallNodeEnd = smallNodeEnd.next
            else:
                newNode = ListNode(node.val)
                biggerNodeEnd.next = newNode
                biggerNodeEnd = biggerNodeEnd.next
            node = node.next
        # 去除原始头结点
        if pHead.val >= x:
            smallNodeHead = smallNodeHead.next
        else:
            biggerNodeHead = biggerNodeHead.next
        # 进行元素拼接
        if biggerNodeHead is None:
            return smallNodeHead
        else:
            smallNodeEnd.next = biggerNodeHead
            return smallNodeHead




p = Partition()
singledLink = p.buildLink()
p.printLink(p.partition(singledLink.getHead(), 5))
