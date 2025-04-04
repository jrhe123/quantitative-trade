class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "#"
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        return dfs(root)

    def deserialize(self, data):
        def dfs(nodes):
            val = next(nodes)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        return dfs(iter(data.split(',')))
    

# Input: root = [1,2,3,null,null,4,5]

# 序列化结果: "1,2,#,#,3,4,#,#,5,#,#"
# 或其他能反序列化出的正确结构的格式