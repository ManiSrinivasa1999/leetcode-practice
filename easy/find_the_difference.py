class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        listOne = [i for i in s]
        listTwo = [i for i in t]
        for i in listOne:
            listTwo.remove(i)
        return listTwo[0]
