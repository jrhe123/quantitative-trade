import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    min_heap = []
    visited = set()
    res = []

    # 初始化堆
    heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
    visited.add((0, 0))

    while min_heap and len(res) < k:
        total, i, j = heapq.heappop(min_heap)
        res.append([nums1[i], nums2[j]])

        # 向右移动：nums1[i+1] + nums2[j]
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

        # 向下移动：nums1[i] + nums2[j+1]
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j + 1))
            visited.add((i, j + 1))

    return res

# 输入：nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出：[[1,2],[1,4],[1,6]]

# 解释：所有的组合为
# [1,2],[1,4],[1,6],
# [7,2],[7,4],[7,6],
# [11,2],[11,4],[11,6]
# 和最小的前三个是：[1,2],[1,4],[1,6]