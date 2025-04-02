from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 1. 先按照起始位置排序
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]  # 初始化结果数组

        for current in intervals[1:]:
            last = merged[-1]

            # 如果当前区间与上一个有重叠
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # 合并
            else:
                merged.append(current)  # 无重叠，加入新区间

        return merged
    
# [[1,3],[2,6],[8,10],[15,18]]


# => [[1,6],[8,10],[15,18]]