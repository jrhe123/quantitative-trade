from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have, need_count = 0, len(need)

        res = ""
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                # 更新最短子串
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1

                # 收缩窗口
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res
    
s = "ADOBECODEBANC"
t = "ABC"

# 给你两个字符串 s 和 t，返回 s 中包含 t 所有字符的最小子串。
# 如果没有这样的子串，返回 ""。
# 字符可能重复，顺序不重要，但频次必须满足。

"BANC"