# 2116 - Check if a Parentheses String Can Be Valid
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        opened = 0
        variable = 0
        for i, char in enumerate(s):
            if locked[i] == "0":
                variable += 1
            elif char == '(':
                opened += 1
            elif char == ')':
                opened -= 1
                if opened == -1:
                    if variable == 0:
                        return False
                    opened += 1
                    variable -= 1
            #print(i, char, opened, variable)
        if (opened + variable ) % 2 == 1:
            return False

        opened = 0
        variable = 0
        for i in range(len(s)-1,-1,-1):
            char = s[i]
            if locked[i] == "0":
                variable += 1
            elif char == ')':
                opened += 1
            elif char == '(':
                opened -= 1
                if opened == -1:
                    if variable == 0:
                        return False
                    opened += 1
                    variable -= 1

        return (opened + variable ) % 2 == 0
