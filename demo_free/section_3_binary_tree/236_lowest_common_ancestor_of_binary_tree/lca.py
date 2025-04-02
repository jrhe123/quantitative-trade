class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果当前节点为空，或遇到 p 或 q，直接返回
        if not root or root == p or root == q:
            return root

        # 在左右子树递归查找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右都非空，说明 p 和 q 分布在左右 → 当前节点是 LCA
        if left and right:
            return root

        # 否则返回非空的那一边
        return left if left else right


#     3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4

# p = 5, q = 1 ➝ 返回 3
# p = 5, q = 4 ➝ 返回 5