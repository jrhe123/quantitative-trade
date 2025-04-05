def subarraysDivByK(nums, k):
    prefix_count = {0: 1}  # 初始化，前缀和 mod k 为 0 出现 1 次
    pre_sum = 0
    count = 0

    for num in nums:
        pre_sum += num
        mod = pre_sum % k

        # Python 对负数取模可能是负的，统一转正
        mod = (mod + k) % k

        # 若当前 mod 出现过，则有多少个前缀使得区间可整除
        count += prefix_count.get(mod, 0)

        # 更新当前 mod 出现次数
        prefix_count[mod] = prefix_count.get(mod, 0) + 1

    return count

# 输入: nums = [4,5,0,-2,-3,1], k = 5
# 输出: 7

# 解释: 子数组个数如下：
# [4,5,0,-2,-3,1], [5,0,-2,-3], [0,-2,-3], [-2,-3], [5], [0], [-3,1]