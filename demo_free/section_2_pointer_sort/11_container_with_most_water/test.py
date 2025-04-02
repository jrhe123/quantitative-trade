# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def max_area(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

if __name__ == "__main__":
    solution = Solution()
    ans = solution.max_area(
        [1,8,6,2,5,4,8,3,7]
    )
    print(ans)