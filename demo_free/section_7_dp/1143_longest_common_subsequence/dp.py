def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# 输入: text1 = "abcde", text2 = "ace"
# 输出: 3  # "ace" 是最长公共子序列

# 输入: text1 = "abc", text2 = "abc"
# 输出: 3

# 输入: text1 = "abc", text2 = "def"
# 输出: 0

