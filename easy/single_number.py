class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newSet = list(set(nums))
        for i in newSet:
            if nums.count(i) == 1:
                return i
