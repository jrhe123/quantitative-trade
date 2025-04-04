from collections import defaultdict

def subarraysDivByK(nums, k):
    mod_count = defaultdict(int)
    mod_count[0] = 1

    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num
        mod = prefix_sum % k
        if mod < 0:  # Python负数取模是负的，需要转正
            mod += k
        result += mod_count[mod]
        mod_count[mod] += 1

    return result

# 输入: nums = [4,5,0,-2,-3,1], k = 5
# 输出: 7

# 解释: 子数组个数如下：
# [4,5,0,-2,-3,1], [5,0,-2,-3], [0,-2,-3], [-2,-3], [5], [0], [-3,1]