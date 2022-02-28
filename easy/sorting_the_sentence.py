class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        d = {}
        for i in l:
            d[i[len(i)-1]] = i[:len(i)-1]
        res = []
        for i in range(1, len(l) + 1):
            res.append(d[str(i)])
        return ' '.join(res)
