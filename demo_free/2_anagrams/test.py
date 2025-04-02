from collections import defaultdict

class Solution:

    def anagrams(self, inputs: list[str]) -> list[list[str]]:
        map = defaultdict(list)
        print("map: ", map)

        for input in inputs:
            key = "".join(sorted(input))
            map[key].append(input)

        return list(map.values())


if __name__ == "__main__":
    ans = Solution().anagrams(
        inputs=["ate", "tea", "eat", "abc", "cba"]
    )
    print(ans)