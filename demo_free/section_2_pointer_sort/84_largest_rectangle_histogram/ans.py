def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # 哨兵柱子

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


# 输入: heights = [2,1,5,6,2,3]
# 输出: 10

# 解释: 5 和 6 可构成宽度为 2，高度为 5 的矩形：5×2 = 10