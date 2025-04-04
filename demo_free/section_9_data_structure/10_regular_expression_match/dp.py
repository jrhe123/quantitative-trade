# 实现一个支持 '.' 和 '*' 的正则表达式匹配函数：
# isMatch(s: str, p: str) -> bool

# '.' 匹配任意单个字符
# '*' 匹配前一个字符的零个或多个重复

# 输入: s = "aa", p = "a" → False  
# 输入: s = "aa", p = "a*" → True （"a*" 可代表 "aa"）  
# 输入: s = "ab", p = ".*" → True （".*" 可代表任意字符串）

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True

    # 初始化：空字符串和以 * 开头的模式
    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # 0 次
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] |= dp[i-1][j]  # 1 次或多次

    return dp[m][n]

# s = "aab"
# p = "c*a*b"

# c* → 匹配 0 次 c → ""
# a* → 匹配 2 次 a → "aa"
# b  → 匹配 b → "b"
# → 成功匹配