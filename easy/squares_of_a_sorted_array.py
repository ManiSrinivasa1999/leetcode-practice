class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [i*i for i in nums]
        return sorted(res)
