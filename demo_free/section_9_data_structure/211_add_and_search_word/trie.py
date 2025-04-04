class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # 是否是一个完整单词的结尾

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)
    

# WordDictionary dict = new WordDictionary()
# dict.addWord("bad")
# dict.addWord("dad")
# dict.addWord("mad")
# dict.search("pad") → False
# dict.search("bad") → True
# dict.search(".ad") → True  # 任意首字母
# dict.search("b..") → True  # 模糊匹配



# dict.addWord("mad")
# dict.search("m.d")

# 搜索过程：
# m → . → 尝试 a~z 所有子节点中是否有有效路径 → d → is_end == True