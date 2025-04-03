import heapq

# heapq.heappush(heap, val)：向堆中插入一个值。
# heapq.heappop(heap)：弹出堆中最小的值。

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0] # 堆顶就是第 k 大的数


# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# 解释：排序后为 [6, 5, 4, 3, 2, 1]，第 2 大是 5

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findKthLargest(
        # nums = [3,2,1,5,6,4], k = 2
        nums = [30,20,10,5,6,4], k = 2
    )
    print(ans)