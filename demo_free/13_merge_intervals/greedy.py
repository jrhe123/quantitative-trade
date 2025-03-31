from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  # 按起始时间排序
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # 合并
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged
    
# [[1,3],[2,6],[8,10],[15,18]]


# => [[1,6],[8,10],[15,18]]