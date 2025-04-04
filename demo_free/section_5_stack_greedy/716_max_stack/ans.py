# 设计一个支持以下操作的栈，满足 部分操作 O(1)，部分操作 O(logN)：

# push(x)：压入元素

# pop()：弹出栈顶

# top()：返回栈顶

# peekMax()：返回栈中的最大值

# popMax()：弹出并返回最大值（若有多个，移除最靠近栈顶的那个）


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer = []

        # 找到最上层的 max
        while self.top() != max_val:
            buffer.append(self.pop())

        # 弹出 max
        self.pop()

        # 把其他值重新压回去
        while buffer:
            self.push(buffer.pop())

        return max_val
