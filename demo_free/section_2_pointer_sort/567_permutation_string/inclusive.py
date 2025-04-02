from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        # 记录 s1 的字符频率
        s1_count = Counter(s1)
        window = Counter()

        for i in range(len2):
            # 加入当前字符
            window[s2[i]] += 1

            # 当窗口超过 s1 的长度时，移除最左边字符
            if i >= len1:
                left_char = s2[i - len1]
                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1

            # 判断窗口是否与 s1 匹配
            if window == s1_count:
                return True

        return False

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: True
# 解释：s2 中的 "ba" 是 s1 的一个排列