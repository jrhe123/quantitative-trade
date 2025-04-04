from collections import defaultdict

class Solution:

    def anagrams(self, inputs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for input in inputs:
            key = "".join(sorted(input))
            result[key].append(input)

        return list(result.values())



if __name__ == "__main__":
    ans = Solution().anagrams(
        inputs=["ate", "tea", "eat", "abc", "cba"]
    )
    print(ans)