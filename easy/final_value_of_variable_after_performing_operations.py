class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plusOne = 'X++'
        plusTwo = '++X'
        plus = 0
        plus += operations.count(plusOne)
        plus += operations.count(plusTwo)
        minusOne = 'X--'
        minusTwo = '--X'
        minus = 0
        minus += operations.count(minusOne)
        minus += operations.count(minusTwo)
        return plus - minus
