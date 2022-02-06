class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        lengths = [len(i) for i in strs]
        minLen = min(lengths)
        for j in range(minLen):
            tempList = []
            for i in strs:
                tempList.append(i[j])
            if len(set(tempList)) == 1:
                prefix += i[j]
            else:
                break
        return prefix
