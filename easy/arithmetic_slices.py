class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        c_d, cnt = -1, 0
        res = 0
        for i in range(1, len(nums)):
            n_d = nums[i] - nums[i - 1]
            if n_d != c_d:
                c_d, cnt = n_d, 1
            else:
                res += cnt
                cnt += 1
        return res
