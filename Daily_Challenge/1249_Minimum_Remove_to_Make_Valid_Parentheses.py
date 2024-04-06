# 1249 - Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        p = -1
        stack = []
        while p < len(s)-1:
            p += 1
            if s[p] == ')' and counter <= 0:
                continue
            elif s[p] == ')':
                counter -= 1
            elif s[p] == '(':
                counter += 1
            stack.append(s[p])
        
        p = len(stack) 
        while counter > 0:
            if stack[p-1] == '(':
                counter -= 1
                del stack[p-1]
            p -= 1

        return "".join(stack)        
