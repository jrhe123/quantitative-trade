from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # 最短至少是自己本身

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# LIS: [2, 3, 7, 101] → 长度是 4