from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1  # 第一个元素总是保留
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow  # 返回新数组的长度
    

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5

# nums 被修改为前 5 个元素为 [0,1,2,3,4]