class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            if s.count(s[i]) < 2:
                return i
        return -1
