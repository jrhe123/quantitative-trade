def maxProduct(nums):
    max_so_far = min_so_far = res = nums[0]

    for num in nums[1:]:
        temp_max = max_so_far  # 先保存旧的最大值

        max_so_far = max(num, num * max_so_far, num * min_so_far)
        min_so_far = min(num, num * temp_max, num * min_so_far)

        res = max(res, max_so_far)

    return res

# 给定一个整数数组 nums，找出一个连续子数组，使得该子数组的乘积最大，返回这个最大值。

# 输入: nums = [2,3,-2,4]
# 输出: 6   # 子数组 [2,3]


# 输入: nums = [-2,0,-1]
# 输出: 0   # 子数组 [0]