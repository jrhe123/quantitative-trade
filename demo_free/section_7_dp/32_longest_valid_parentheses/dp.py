# 🧩 题目描述：
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的 有效（括号匹配）子串 的长度。


def longestValidParentheses(s):
    n = len(s)
    dp = [0] * n
    max_len = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2
                if i - dp[i - 1] >= 2:
                    dp[i] += dp[i - dp[i - 1] - 2]
        max_len = max(max_len, dp[i])

    return max_len


# 输入: "(()"
# 输出: 2  # "()"

# 输入: ")()())"
# 输出: 4  # "()()"

# 输入: ""
# 输出: 0


# 位置： 0 1 2 3 4 5
# 字符串：) ( ) ( ) )
# dp:     0 0 2 0 4 0
#         ↑     ↑
# 最大匹配长度是 4