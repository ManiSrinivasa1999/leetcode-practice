class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                u = min(nums1.count(i), nums2.count(i))
                for _ in range(u):
                    res.append(i)
        return res
