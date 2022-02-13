# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        ans = n

        while low <= high:
            mid = (low+high)//2

            if isBadVersion(mid) == False:
                low = mid+1

            elif isBadVersion(mid) == True:
                high = mid-1
                ans = mid

        return ans
