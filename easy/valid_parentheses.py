class Solution:
    def isValid(self, s: str) -> bool:
        openBrac = '({['
        closing = ']})'
        par = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in s:
            if i in openBrac:
                stack.append(i)
            elif i in closing:
                if len(stack) == 0:
                    return False
                if stack[-1] == par[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
