from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)

        res = []

        # 遍历所有偏移起点
        for i in range(word_len):
            left = i
            right = i
            window_count = Counter()
            words_used = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # 当前词在词表中
                if word in word_count:
                    window_count[word] += 1
                    words_used += 1

                    # 多了就收缩窗口
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    # 如果正好用完所有词，记录结果
                    if words_used == num_words:
                        res.append(left)

                else:
                    # 词不在词表中，窗口重置
                    window_count.clear()
                    words_used = 0
                    left = right

        return res
    

# Input:
# s = "barfoothefoobarman"
# words = ["foo","bar"]

# Output: [0, 9]

# 解释：从 0 开始的 "barfoo"，从 9 开始的 "foobar"