import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap（用负数模拟）
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        # 将最大堆堆顶移动到最小堆
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 平衡堆大小（最大堆多一个或相等）
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.findMedian()  # 返回 1.5
mf.addNum(3)
mf.findMedian()  # 返回 2


# 输入：
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[],             [1],      [2],       [],          [3],      []]

# 输出：
# [null, null, null, 1.5, null, 2.0]