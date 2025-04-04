# 你有 W 初始资本，可以最多做 k 个项目。
# 每个项目需要 capital[i] 才能启动，完成后能赚 profits[i]。

# 你只能在当前资本 W ≥ 启动资金要求的项目中选择。

# 目标是：在最多做 k 个项目的前提下，让最终资本最大。


import heapq

def findMaximizedCapital(k, W, profits, capital):
    min_cap_heap = []  # 所有项目，按 capital 升序
    max_profit_heap = []  # 可启动项目，按 profit 降序（用负数模拟大顶堆）

    # Step 1: 构造最小堆（启动资金要求）
    for c, p in zip(capital, profits):
        heapq.heappush(min_cap_heap, (c, p))

    # Step 2: 执行最多 k 次
    for _ in range(k):
        # 把所有可以做的项目放进最大利润堆
        while min_cap_heap and min_cap_heap[0][0] <= W:
            c, p = heapq.heappop(min_cap_heap)
            heapq.heappush(max_profit_heap, -p)  # 利润大顶堆

        if not max_profit_heap:
            break  # 没有可做的项目

        W += -heapq.heappop(max_profit_heap)  # 做利润最大的项目

    return W




# 输入: k = 2, W = 0, Profits = [1,2,3], Capital = [0,1,1]
# 输出: 4
# 解释: 先启动项目 0（赚 1），资本变为 1，再启动项目 1 或 2（赚 2 或 3），总资本最多为 4。