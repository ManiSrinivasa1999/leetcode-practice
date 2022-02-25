class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rw = []
        for i in accounts:
            s = 0
            for j in i:
                s += j
            rw.append(s)
        return max(rw)
