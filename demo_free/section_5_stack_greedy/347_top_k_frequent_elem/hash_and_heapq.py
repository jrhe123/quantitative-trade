from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计每个元素出现的频率
        freq = Counter(nums)  # 返回字典：{num: count}

        # 2. 构建最小堆，key 是频率
        # heapq.nlargest：从 freq.items() 中选出 k 个频率最大的元素
        top_k = heapq.nlargest(k, freq.items(), key=lambda x: x[1])

        # 3. 提取前 k 个元素（只要数字，不要频率）
        return [num for num, _ in top_k]


# Input:
# nums = [1,1,1,2,2,3]
# k = 2

# Output:
# [1, 2]
