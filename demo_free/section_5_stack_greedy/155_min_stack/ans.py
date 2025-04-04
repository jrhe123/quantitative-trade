# 设计一个栈，支持以下操作，所有操作时间复杂度为 O(1)：

# push(x)：压入元素

# pop()：弹出栈顶元素

# top()：获取栈顶元素

# getMin()：获取栈中最小元素（实时）

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 若空栈或新值更小，更新 min 栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]