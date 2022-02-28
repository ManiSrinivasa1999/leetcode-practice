class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = 0
        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        elif ruleKey == 'name':
            key = 2
        res = 0
        for i in items:
            if i[key] == ruleValue:
                res += 1
        return res
