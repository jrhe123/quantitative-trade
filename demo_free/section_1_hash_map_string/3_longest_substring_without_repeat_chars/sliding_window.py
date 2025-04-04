class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 记录窗口内的字符
        left = 0          # 窗口左边界
        max_len = 0       # 最大长度

        for right in range(len(s)):
            # 当右边字符重复时，移动左边指针
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])  # 加入当前字符
            max_len = max(max_len, right - left + 1)  # 更新最大长度

        return max_len

# 输入: s = "abcabcbb"

# right=0, c='a' → 无重复 → max_len=1
# right=1, c='b' → 无重复 → max_len=2
# right=2, c='c' → 无重复 → max_len=3
# right=3, c='a' → 出现重复，left=1
# right=4, c='b' → 出现重复，left=2
# ...
# 最终 max_len = 3
