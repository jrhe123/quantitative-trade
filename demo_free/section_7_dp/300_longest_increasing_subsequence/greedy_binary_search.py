import bisect

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)


# 输入: nums = [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长递增子序列是 [2,3,7,101]


# 输入: nums = [0,1,0,3,2,3]
# 输出: 4
