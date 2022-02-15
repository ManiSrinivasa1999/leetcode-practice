class Solution:
    def reverseWords(self, s: str) -> str:
        string = []
        res = ''
        for i in s:
            if i == ' ':
                res += ''.join(string[::-1])
                res += ' '
                string = []
            else:
                string.append(i)
        res += ''.join(string[::-1])
        return res
