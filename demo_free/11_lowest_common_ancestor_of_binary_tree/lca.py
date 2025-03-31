class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
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