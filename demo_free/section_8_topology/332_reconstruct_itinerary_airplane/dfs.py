# 给你一个机票列表 tickets，每张票是一个 [from, to] 的字符串对，代表从一个机场飞到另一个机场。

# 你从 "JFK" 出发，使用所有机票恰好一次。

# 要求构造一个字典序最小的有效行程。

# 保证至少有一个有效行程。



from collections import defaultdict
import heapq

def findItinerary(tickets):
    graph = defaultdict(list)

    # 构建邻接表 + 小根堆保证字典序
    for src, dest in tickets:
        heapq.heappush(graph[src], dest)

    res = []

    def dfs(node):
        while graph[node]:
            next_dest = heapq.heappop(graph[node])
            dfs(next_dest)
        res.append(node)  # 后序插入

    dfs("JFK")
    return res[::-1]  # 逆序得到答案


# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 路径选取：
# JFK → ATL → JFK → SFO → ATL → SFO