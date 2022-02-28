class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = {}
        for i in range(len(s)):
            res[indices[i]] = s[i]
        r = ''
        for i in range(len(s)):
            r += res[i]
        return r
