# [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# 输出：3
# 解释：有三个岛屿（左上、中央、右下）

class Solution:
    def number_of_islands(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        count = 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
                return
            
            grid[r][c] = '0'

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count

if __name__ == "__main__":
    solution = Solution()
    ans = solution.number_of_islands(
        [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
    )
    print("ans: ", ans)