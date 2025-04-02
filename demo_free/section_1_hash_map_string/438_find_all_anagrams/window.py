from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []

        res = []
        p_count = Counter(p)
        window = Counter()

        for i in range(len_s):
            window[s[i]] += 1

            # 窗口超出长度限制，左边字符要移除
            if i >= len_p:
                left_char = s[i - len_p]
                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1

            # 当前窗口字符频率匹配 p
            if window == p_count:
                res.append(i - len_p + 1)

        return res
    
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]

# 解释：s[0:3] = "cba" 是 "abc" 的排列，s[6:9] = "bac" 也是