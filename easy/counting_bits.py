class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            c = str(bin(i)).count('1')
            res.append(c)
        return res
