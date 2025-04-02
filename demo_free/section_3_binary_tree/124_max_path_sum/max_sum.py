from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # 初始化全局最大路径和

        def dfs(node: TreeNode | None):
            if not node:
                return 0

            # 左右子树最大路径贡献值（小于 0 就不要了）
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # 当前节点为“弯道”时的路径值
            current_path = node.value + left_gain + right_gain

            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, current_path)

            # 向上传递：只能选一边
            return node.value + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
