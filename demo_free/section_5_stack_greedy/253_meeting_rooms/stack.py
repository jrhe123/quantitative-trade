import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])

        # 最小堆：保存当前正在使用会议室的会议的结束时间
        heap = []

        for interval in intervals:
            start, end = interval

            # 如果当前会议可以复用最早结束的会议室（结束时间 ≤ 当前开始时间）
            if heap and heap[0] <= start:
                heapq.heappop(heap)  # 弹出旧会议

            heapq.heappush(heap, end)  # 安排当前会议
            print("heap: ", heap)

        return len(heap)  # 堆的大小 = 会议室数量


# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# heap:  [30]
# heap:  [10, 30]
# heap:  [20, 30]

# 解释：
# - 会议 [0,30] 与 [5,10] 冲突 → 需要两间会议室
# - [15,20] 可复用第二间会议室

solution = Solution()
ans = solution.minMeetingRooms(
    [[0,30],[5,10],[15,20]]
)
print(ans)
