from collections import Counter

def findAnagrams(s, p):
    need = Counter(p)
    window = Counter(s[:len(p)])
    res = []

    if need == window:
        res.append(0)

    for i in range(len(p), len(s)):
        window[s[i]] += 1

        left_char = s[i - len(p)]
        window[left_char] -= 1

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