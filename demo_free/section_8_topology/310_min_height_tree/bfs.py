# 给定一个包含 n 个节点的无向图（是一棵树），找出所有可以成为根节点，使整棵树的高度最小。

# 输入: n = 4, edges = [[1,0],[1,2],[1,3]]
# 输出: [1]
# 解释: 以节点 1 为根，高度为 1。其他节点为根高度都更大。

# 输入: n = 6, edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]
# 输出: [3,4]

from collections import defaultdict, deque

def findMinHeightTrees(n, edges):
    if n <= 2:
        return list(range(n))

    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # 初始化叶子节点
    leaves = [i for i in range(n) if len(graph[i]) == 1]

    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []

        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves


# edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]
# 初始叶子：0,1,2,5 → 剥掉 → 剩余：3,4
# 再次剥掉 3 → 只剩 4
# 最终返回 [3,4]