def subarraySum(nums, k):
    from collections import defaultdict

    count_map = defaultdict(int)
    count_map[0] = 1  # 初始化前缀和为0的情况

    pre_sum = 0
    result = 0

    for num in nums:
        pre_sum += num
        result += count_map[pre_sum - k]  # 找有多少前缀和满足条件
        count_map[pre_sum] += 1  # 更新前缀和出现次数

    return result

# 输入: nums = [1,1,1], k = 2
# 输出: 2
# 解释: 子数组 [1,1] 出现了两次

# 输入: nums = [1,2,3], k = 3
# 输出: 2  # [1,2] 和 [3]