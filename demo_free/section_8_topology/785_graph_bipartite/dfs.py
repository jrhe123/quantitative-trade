def isBipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 表示未染色

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False

    return True


# 输入: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# 输出: False
# 解释: 不能将节点分成两个集合使每条边都连接不同集合


# 输入: graph = [[1,3],[0,2],[1,3],[0,2]]
# 输出: True


# 二分图定义：图中的所有相邻节点都必须有不同的“颜色”（可以用 0 和 1 表示两种颜色）

