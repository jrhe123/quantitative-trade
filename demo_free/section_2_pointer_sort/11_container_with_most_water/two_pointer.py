# 🎯 核心逻辑：
# 设两个指针 left 和 right，从数组两端向中间移动

# 容器面积 = min(height[left], height[right]) * (right - left)

# 哪边低，就移动哪边（希望找到更高的边）

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # 当前容器的面积
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            # 移动短板
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
    
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxArea(
        [1,8,6,2,5,4,8,3,7]
    )
    print(ans)