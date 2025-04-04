# 设计一个 PeekingIterator 类，在已有迭代器的基础上添加一个 peek() 方法，使其可以查看下一个元素而不移动指针。

# 该类应支持以下操作：

# peek()：查看下一个元素（不前进指针）

# next()：返回下一个元素，并移动指针

# hasNext()：是否还有元素

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._has_next = True
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._has_next = False
            self._next = None

    def peek(self):
        return self._next

    def next(self):
        curr = self._next
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._has_next = False
            self._next = None
        return curr

    def hasNext(self):
        return self._has_next