class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            # 从中心向两边扩展
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回当前找到的回文子串
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            # 奇数长度回文（一个字符为中心）
            odd = expandAroundCenter(i, i)
            # 偶数长度回文（两个字符为中心）
            even = expandAroundCenter(i, i + 1)

            # 更新最长回文
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
    
if __name__ == "__main__":
    ans = Solution().longestPalindrome(
        "babad"
    )
    print("ans: ", ans)