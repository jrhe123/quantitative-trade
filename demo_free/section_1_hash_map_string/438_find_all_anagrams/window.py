from collections import Counter
from typing import List

def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    need = Counter(p)               # 目标字符频率
    window = Counter(s[:len(p)])   # 初始化第一个窗口
    res = []

    if window == need:
        res.append(0)

    for i in range(len(p), len(s)):
        # 加入新字符
        window[s[i]] += 1

        # 移除左边的字符（滑动窗口）
        left_char = s[i - len(p)]
        window[left_char] -= 1
        # 清空为0
        if window[left_char] == 0:
            del window[left_char]

        if window == need:
            res.append(i - len(p) + 1)

    return res
    
# s = "cbaebabacd", p = "abc"
# 目标频率：{'a':1, 'b':1, 'c':1}

# i=0: "cba" ✔
# i=1: "bae" ✘
# i=6: "bac" ✔