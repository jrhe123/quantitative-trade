from collections import Counter

class Solution:
    def min_window_substring(self, string: str, sub_string: str):
        need = Counter(sub_string)
        window = {}
        have = 0
        need_count = len(need)

        res = ""
        res_len = float("inf")
        left = 0

        for right in range(len(string)):
            c = string[right]
            window[c] = window.get(c, 0) + 1

            if c in need and need[c] == window[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = string[left: right+1]

                window[string[left]] -= 1

                if string[left] in need and window[string[left]] < need[string[left]]:
                    have -= 1

                left += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    ans = solution.min_window_substring(
        string="ADOBECODEBANC",
        sub_string="ABC"
    )
    print("ans: ", ans)