#  解题思路：单调队列（Monotonic Queue）
# ✅ 单调队列的作用：
# 我们维护一个 单调递减队列（队头最大）：

# 每次新元素加入时，把队列末尾比它小的全部弹出

# 队首是当前窗口最大值

# 如果队首已经滑出窗口，移除它


from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # 存索引而不是值

    for i in range(len(nums)):
        # 1. 清除队尾所有比当前值小的
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # 2. 移除队首元素（已滑出窗口）
        if dq[0] <= i - k:
            dq.popleft()

        # 3. 收集结果（i >= k - 1 才开始有窗口）
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

#! 给定一个整数数组 nums 和一个滑动窗口大小 k，返回每个滑动窗口中的最大值。

# 输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出: [3,3,5,5,6,7]

# 解释:
# 窗口依次为：
# [1 3 -1] → 3  
# [3 -1 -3] → 3  
# [-1 -3 5] → 5  
# [-3 5 3] → 5  
# [5 3 6] → 6  
# [3 6 7] → 7