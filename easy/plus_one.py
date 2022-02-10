class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sumOfDigits = 0
        for i in range(len(digits) - 1, -1, -1):
            sumOfDigits += digits[len(digits) - 1 - i] * (10**i)
        sumOfDigits += 1
        res = []
        for i in str(sumOfDigits):
            res.append(i)
        return res
