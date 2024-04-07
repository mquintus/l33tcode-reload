# 678 - Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = s.count("*")
        left_count = s.count("(")
        right_count = s.count(")")
        if abs(left_count - right_count) > star_count:
            return False
        
        opened = 0
        for el in s:
            if el in '(*':
                opened += 1
            elif el == ')':
                if opened > 0:
                    opened -= 1
                else:
                    return False
        
        opened = 0
        for el in s[::-1]:
            if el in '*)':
                opened += 1
            elif el == '(':
                if opened > 0:
                    opened -= 1
                else:
                    return False

        return True
