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

s = "abcabcbb"
