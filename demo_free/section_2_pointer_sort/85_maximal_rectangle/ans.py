def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        heights.append(0)  # 加一个哨兵，确保栈清空

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            stack.append(i)
        heights.pop()  # 移除哨兵
        return max_area

    cols = len(matrix[0])
    heights = [0] * cols
    max_rect = 0

    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == "1" else 0
        max_rect = max(max_rect, largestRectangleArea(heights))

    return max_rect




# 输入:
# matrix = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]

# 输出: 6
# 解释：最大矩形在中间一块 2 行 × 3 列