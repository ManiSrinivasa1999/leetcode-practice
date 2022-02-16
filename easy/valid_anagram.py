class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = [i for i in s]
        tList = [i for i in t]
        sList.sort()
        tList.sort()
        return sList == tList
