from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            # 把字符串排序，作为 key
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(strs))