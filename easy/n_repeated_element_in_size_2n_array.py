class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        existingElements = []
        for i in nums:
            if i not in existingElements:
                existingElements.append(i)
            else:
                return i
