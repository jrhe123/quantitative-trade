from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0  # 如果输入是空的，直接返回0
        if len(nums) == 1: return nums[0]  # 如果只有一个房子，只能偷它

        prev1, prev2 = 0, 0  # 初始化两个变量，分别表示 dp[i-1] 和 dp[i-2]
        for num in nums:
            curr = max(prev1, prev2 + num)  # 状态转移：当前最大值是偷或不偷
            prev2 = prev1  # 更新 prev2 → 上一轮的 prev1
            prev1 = curr   # 更新 prev1 → 当前最大值
        return prev1  # 返回最终的最大收益
    
# 你是一个小偷，计划偷一排房子，每个房子有一定金额 nums[i]。
# 但是相邻的房子不能同时偷，否则会触发警报。
# 请你计算：能偷到的最大金额是多少？


# nums = [2, 7, 9, 3, 1]
# 偷第 1 和第 3 和第 5：2 + 9 + 1 = 12
# 偷第 2 和第 4：7 + 3 = 10 → 返回最大值：12

