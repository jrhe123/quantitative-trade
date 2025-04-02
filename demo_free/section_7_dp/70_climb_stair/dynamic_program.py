class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        print("dp: ", dp)
        return dp[n]
    
if __name__ == "__main__":
    solution = Solution()
    ans = solution.climbStairs(5)
    print("ans: ", ans)
    
# n = 5
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 8
#! 所以输出是 8

# 假设你正在爬楼梯。每次你可以爬 1 步或 2 步。
# 给你一个正整数 n，表示楼梯总共有 n 阶。求你有多少种不同的方法爬到楼顶。


# 想爬到第 n 阶，你可以从：
# 第 n - 1 阶爬 1 步上来
# 第 n - 2 阶爬 2 步上来
# dp[n] = dp[n-1] + dp[n-2]