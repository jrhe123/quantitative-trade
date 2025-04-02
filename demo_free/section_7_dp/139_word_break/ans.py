from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # 将词典转换为集合，加快查找速度 O(1)
        n = len(s)
        dp = [False] * (n + 1)    # dp[i] 表示 s[0:i] 是否可以拆分
        dp[0] = True              # 空字符串可以认为是被成功拆分的

        for i in range(1, n + 1):         # 遍历 s 的每个前缀
            for j in range(i):           # 再遍历每个前缀 s[0:j]
                if dp[j] and s[j:i] in word_set:  # s[0:j] 可以拆分，且 s[j:i] 是词典中的词
                    dp[i] = True
                    break                # 一旦找到一种方式就可以了，退出内部循环

        return dp[n]  # 返回整个字符串是否可以被拆分
    
s = "leetcode"
wordDict = ["leet", "code"]

# dp[4] = True（"leet"）

# dp[8] = True（"code"）
# → 返回 True

