from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagram_v2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch1, ch2 in zip(s, t):
            count[ord(ch1) - ord('a')] += 1
            count[ord(ch2) - ord('a')] -= 1

        return all(c == 0 for c in count)


# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False