class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = []
        for i in sentences:
            temp = i.split(' ')
            count.append(len(temp))
        return max(count)
