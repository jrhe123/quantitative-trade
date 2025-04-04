from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque()
    queue.append((beginWord, 1))  # (当前单词, 当前步数)

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    queue.append((new_word, steps + 1))
                    word_set.remove(new_word)  # 避免重复访问

    return 0


# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# 输出: 5
# 解释: hit -> hot -> dot -> dog -> cog（共 5 步）