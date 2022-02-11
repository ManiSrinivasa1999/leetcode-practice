class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # lst = []
        # for i in nums:
        #     if i not in lst:
        #         lst.append(i)
        #     else:
        #         return True
        # return False
        return len(nums) != len(set(nums))
