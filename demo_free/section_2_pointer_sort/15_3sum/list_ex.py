from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序是去重和双指针的基础
        res = []
        n = len(nums)

        for i in range(n):
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 跳过重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif s < 0:
                    left += 1  # 需要更大的数
                else:
                    right -= 1  # 需要更小的数

        return res


# Input:
# nums = [-1, 0, 1, 2, -1, -4]

# Output:
# [[-1, -1, 2], [-1, 0, 1]]