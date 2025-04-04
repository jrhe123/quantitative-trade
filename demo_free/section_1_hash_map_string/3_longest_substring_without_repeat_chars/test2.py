class Solution:
    def longest_substring_without_repeat_chars(self, input: str):
        char_set = set()
        max_len = 0
        left = 0

        for right in range(len(input)):
            while input[right] in char_set:
                char_set.remove(input[left])
                left += 1

            char_set.add(input[right])
            max_len = max(max_len, right - left + 1)

        return max_len