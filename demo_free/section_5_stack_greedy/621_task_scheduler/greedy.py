from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for val in freq.values() if val == max_freq)

        # 公式：关键是安排 (max_freq - 1) 段，每段长度 n + 1，加上 max_count 个尾巴
        intervals = (max_freq - 1) * (n + 1) + max_count

        # 实际任务量可能比空格加任务更多 → 取最大值
        return max(len(tasks), intervals)
    
tasks = ["A","A","A","B","B","B"], n = 2

# A B idle A B idle A B
# 输出：8