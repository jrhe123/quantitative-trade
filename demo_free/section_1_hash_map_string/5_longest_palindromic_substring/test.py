class Solution:
    def longest_palindromic_substring(self, input: str) -> str:

        def expand_from_center(left, right):
            while left >= 0 and right < len(input) and input[left] == input[right]:
                left -= 1
                right += 1

            return input[left+1, right]
        
        longest = ""

        for i in range(len(input)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest