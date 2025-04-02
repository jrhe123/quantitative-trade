from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 defaultdict 自动初始化列表
        anagram_map = defaultdict(list)

        for word in strs:
            # 对每个单词进行排序，并将其作为 key
            sorted_word = ''.join(sorted(word))  # 排序后的字符串
            anagram_map[sorted_word].append(word)  # 加入同组

        # 最终返回所有分组结果（dict 的值）
        return list(anagram_map.values())
