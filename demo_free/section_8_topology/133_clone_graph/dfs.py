class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(node):
    if not node:
        return None

    old_to_new = {}

    def dfs(cur):
        if cur in old_to_new:
            return old_to_new[cur]

        # 克隆当前节点
        copy = Node(cur.val)
        old_to_new[cur] = copy

        # 克隆所有邻居
        for neighbor in cur.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)