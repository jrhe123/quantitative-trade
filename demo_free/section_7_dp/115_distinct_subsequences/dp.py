# 🧩 题目描述：
# 给定两个字符串 s 和 t，返回 s 中有多少个子序列等于 t。

# 子序列是可以删除任意个字符（不改变顺序）形成的新字符串。


# 输入: s = "rabbbit", t = "rabbit"
# 输出: 3  
# 解释: 有三个不同方式从 s 中形成 t：
# - rab_bbit
# - ra_b_bbit
# - rabb_bit

def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 1  # 匹配空串的方式都是 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][n]