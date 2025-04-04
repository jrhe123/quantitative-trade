from collections import deque

def maxSlidingWindow(nums, k):
    queue = deque()
    result = []

    for i in range(len(nums)):

        # pop the queue until it's greater than current num
        # 清理queue
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)

        if queue[0] <= i - k:
            queue.popleft()

        print("queue: ", queue)

        #  >= k - 1 才开始有窗口
        if i >= k - 1:
            result.append(nums[queue[0]])
    
    return result


output = maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(output)

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