class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            temp = extraCandies + candies[i]
            if temp >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
