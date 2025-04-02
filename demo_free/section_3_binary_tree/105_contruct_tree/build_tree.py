from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # 哈希表优化中序查找：值 → 下标
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            # 前序首元素为根
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # 根在中序中的位置
            index = inorder_map[root_val]
            left_size = index - in_left

            # 构造左子树
            root.left = build(
                pre_left + 1, 
                pre_left + left_size, 
                in_left, 
                index - 1
            )
            # 构造右子树
            root.right = build(
                pre_left + left_size + 1, 
                pre_right, 
                index + 1, 
                in_right
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
