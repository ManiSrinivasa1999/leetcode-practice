class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            t = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and i != j:
                    t += 1
            res.append(t)
        return res
