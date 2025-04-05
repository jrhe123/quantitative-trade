def contain_most_water(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

