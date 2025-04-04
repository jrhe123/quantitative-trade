from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}  # 所有字符

    # Step 1: 建图
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        # 检查非法前缀情况
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break  # 只找第一个不同字符

    # Step 2: 拓扑排序 BFS
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    res = []

    while queue:
        c = queue.popleft()
        res.append(c)
        for nei in graph[c]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return "".join(res) if len(res) == len(in_degree) else ""




# 输入: ["wrt", "wrf", "er", "ett", "rftt"]
# 输出: "wertf"


# 解释: 
# - "wrt" 在 "wrf" 之前 → 't' < 'f'
# - "wrf" 在 "er" 之前 → 'w' < 'e'
# - "er" 在 "ett" 之前 → 'r' < 't'
# - "ett" 在 "rftt" 之前 → 'e' < 'r'