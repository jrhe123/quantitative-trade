class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        # 按右边界升序排序
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]  # 第一支箭的位置

        for x_start, x_end in points[1:]:
            # 若当前气球起点 > 箭位置 → 需要新箭
            if x_start > end:
                arrows += 1
                end = x_end  # 更新箭位置

        return arrows


# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2

# 解释：
# - 第一支箭射在 x=6：击中 [2,8], [1,6]
# - 第二支箭射在 x=16：击中 [10,16], [7,12]