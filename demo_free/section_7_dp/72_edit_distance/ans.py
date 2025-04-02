class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 初始化 dp 表，大小 (m+1) x (n+1)

        for i in range(m + 1):
            dp[i][0] = i  # word2 为空时，只能删除 word1 的字符
        for j in range(n + 1):
            dp[0][j] = j  # word1 为空时，只能插入 word2 的字符

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不需操作
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # 删除 word1[i-1]
                        dp[i][j - 1],     # 插入 word2[j-1]
                        dp[i - 1][j - 1]  # 替换 word1[i-1] 为 word2[j-1]
                    )

        return dp[m][n]
    
word1 = "horse"
word2 = "ros"

# horse → ros 最少需要 3 步操作：
# horse → rorse (替换 'h' → 'r')
# rorse → rose (删除 'r')
# rose → ros (删除 'e')

# => 3