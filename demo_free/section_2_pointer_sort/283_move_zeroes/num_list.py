from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        # 1. 将非零元素往前移
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # 2. 把剩余位置置为 0
        for i in range(slow, len(nums)):
            nums[i] = 0

# 这是“原地修改”，不返回新数组。
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]