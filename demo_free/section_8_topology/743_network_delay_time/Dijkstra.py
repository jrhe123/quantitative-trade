# 你有一个 n 个节点的网络，编号从 1 到 n，给定边集 times，表示每条边 (u, v, w)：

# 从节点 u 到节点 v，需要时间 w

# 从源节点 k 发送一条信号，返回 所有节点收到信号的最早时间。
# 如果无法触达所有节点，返回 -1。



import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    heap = [(0, k)]  # (当前时间, 当前节点)
    dist = {}  # 节点最短到达时间

    while heap:
        time, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = time
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (time + w, nei))

    return max(dist.values()) if len(dist) == n else -1