from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: TreeNode | None):
            if not node:
                return

            dfs(node.left)         # 1. 遍历左子树
            res.append(node.val)   # 2. 访问当前节点
            dfs(node.right)        # 3. 遍历右子树

        dfs(root)
        return res
    
# Input:
#     1
#      \
#       2
#      /
#     3

# Output: [1, 3, 2]