def maxSubArray(nums):
    curr_max = global_max = nums[0]
    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        global_max = max(global_max, curr_max)
    return global_max



# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6

# 解释: 子数组 [4,-1,2,1] 的和最大，为 6