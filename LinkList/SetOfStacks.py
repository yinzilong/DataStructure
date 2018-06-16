# -*- coding:utf-8 -*-
# 一个二维数组，每一行是一个栈
# 每个栈大小为size，即列数目为size
# push操作，push时，最后一个栈的满了，增加一个行并入栈
# pop操作，pop最后一行的栈顶，如果最后一行栈空，就pop掉最后一行，再pop倒数第二行的栈顶
class SetOfStacks:
    def __init__(self):
        self.stack = []
        self.size = None

    # ope代表操作
    # ope[0]==1表示push，ope[0]==2表示pop
    def setOfStacks(self, ope, size):
        self.size = size
        if ope is None:
            return None
        else:
            for operation in ope:
                if operation[0] == 1:
                    self.push(operation[1])
                elif operation[0] == 2:
                    self.pop()
        return stacks

    def push(self, node):
        if not self.stack:
            self.stack.append([])
        if len(self.stack[-1]) == self.size:
            self.stack.append([])
            self.stack[-1].append(node)
        else:
            self.stack[-1].append(node)

    def pop(self):
        if len(self.stack[-1]) == 0:
            self.stack.pop()
            if len(self.stack) == 0:  # 倒数第二个栈也为空，那么就表示栈集合已经没有元素
                return None
        else:
            self.stack[-1].pop()

ope =[[1,97868],[1,69995],[1,28525],[1,72341],[1,86916],[1,5966],[2,58473],[2,93399],[1,84955],[1,16420],[1,96091],[1,45179],[1,59472],[1,49594],[1,67060],[1,25466],[1,50357],[1,83509],[1,39489],[2,51884],[1,34140],[1,8981],[1,50722],[1,65104],[1,61130],[1,92187],[2,2191],[1,2908],[1,63673],[2,92805],[1,29442]]
size =2
stacks = SetOfStacks()
print(stacks.setOfStacks(ope, size))