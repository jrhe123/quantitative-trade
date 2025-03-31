from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # 统计频率
        return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


nums = [1,1,1,2,2,3]
k = 2

