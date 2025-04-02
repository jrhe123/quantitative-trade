from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)          # 统计 t 中每个字符的需求
        window = {}                # 记录当前窗口字符频率
        have = 0                   # 已满足的字符种类数
        need_count = len(need)     # 需要满足的总字符种类数

        res = ""
        res_len = float("inf")     # 初始化最小窗口长度为无穷大
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # 如果这个字符是需要的，并且数量刚刚达到
            if c in need and window[c] == need[c]:
                have += 1

            # 当窗口已经满足所有条件，开始尝试收缩左边
            while have == need_count:
                # 更新最优解
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1

                # 左指针缩小窗口
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