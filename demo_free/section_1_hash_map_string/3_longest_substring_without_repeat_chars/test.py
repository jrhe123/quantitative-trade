class Solution:
    def longest_substring(self, input: str) -> int:
        n = len(input)
        left = 0
        char_set = set()
        max_len = 0

        for right in range(n):
            if input[right] in char_set:
                char_set.remove(input[left])
                left += 1

            char_set.add(input[right])
            max_len = max(max_len, right - left + 1)

        return max_len



if __name__ == "__main__":
    ans = Solution().longest_substring(
        input="abcdbcbb"
    )
    print(ans)
