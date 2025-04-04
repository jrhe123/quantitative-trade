from collections import Counter
from typing import List

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)  # 原始单词频率

    res = []

    # 我们从每个 offset 起点滑动（因为可能错位）
    for i in range(word_len):
        left = i
        right = i
        curr_count = 0
        window = {}

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len

            # 如果是有效单词，加入窗口
            if word in word_freq:
                window[word] = window.get(word, 0) + 1
                curr_count += 1

                # 如果某个单词过多，缩小窗口
                while window[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    curr_count -= 1

                # 匹配成功
                if curr_count == word_count:
                    res.append(left)

            else:
                # 非法单词，重置窗口
                window.clear()
                curr_count = 0
                left = right

    return res
    

# s = "barfoothefoobarman"
# words = ["foo", "bar"]
# → 目标窗口长度 = 6

# i = 0: "barfoo" → 有效 ✔
# i = 1: "arfoot" → 无效 ✘
# i = 3: "foothe" → 无效 ✘
# ...
# i = 9: "foobar" → 有效 ✔