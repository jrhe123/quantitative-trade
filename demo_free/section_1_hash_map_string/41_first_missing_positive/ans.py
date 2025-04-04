# 对于一个长度为 n 的数组，答案一定在 [1, n+1] 范围内。
# 我们可以用索引为 key，元素值为 presence 状态来标记哪些数字存在。

def firstMissingPositive(nums):
    n = len(nums)

    # Step 1: 预处理
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: 原地哈希标记
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Step 3: 查找第一个未标记的位置
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1


# nums = [3, 4, -1, 1]

# Step 1: 替换负数 → [3, 4, 5, 1]  
# Step 2: 标记出现过的数字 → index 2, 3, 0 → nums = [-3, 4, -5, -1]  
# Step 3: 找第一个 >0 的位置是 index 1 → 答案是 2