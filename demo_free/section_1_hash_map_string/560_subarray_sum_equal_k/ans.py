def subarraySum(nums, k):
    prefix_count = {0: 1}  # 初始化：前缀和为 0 出现一次（空子数组）
    pre_sum = 0
    count = 0

    for num in nums:
        print("pre_sum: ", pre_sum)
        pre_sum += num  # 当前前缀和

        # 查找之前是否有 pre_sum - k 出现过
        if pre_sum - k in prefix_count:
            count += prefix_count[pre_sum - k]

        # 更新当前前缀和的出现次数
        prefix_count[pre_sum] = prefix_count.get(pre_sum, 0) + 1

    print("prefix_count: ", prefix_count)

    return count

subarraySum(
    [1,1,1], 2
)

# 输入: nums = [1,1,1], k = 2
# 输出: 2
# 解释: 子数组 [1,1] 出现了两次

# 输入: nums = [1,2,3], k = 3
# 输出: 2  # [1,2] 和 [3]