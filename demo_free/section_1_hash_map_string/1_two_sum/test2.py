# nums = [2, 7, 11, 15]
# target = 9

class Solution:
    def two_sum(self, nums: list[int], target: int):
        lookup = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            
            lookup[num] = i
        
        return []
