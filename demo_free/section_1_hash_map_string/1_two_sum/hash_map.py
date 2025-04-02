from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建哈希表，用于存储数字和对应的索引
        lookup = {}

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算当前数字需要的补数
            complement = target - num

            # 如果补数已经在哈希表中，说明找到了答案
            if complement in lookup:
                return [lookup[complement], i]

            # 否则将当前数字加入哈希表
            lookup[num] = i

        # 如果没有答案（根据题意不会发生），可以返回空列表
        return []
