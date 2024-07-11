# 1190 - Reverse Substrings Between Each Pair of Parentheses
class Solution:
    def reverseParentheses(self, s: str) -> str:
        def rev(start):
            nonlocal s
            result = ""
            i = start
            while i < len(s):
                if s[i] == '(':
                    localresult = '(' + rev(i+1)
                    i += len(localresult)
                    result += localresult[::-1]
                elif s[i] == ')':
                    return result + ')'
                else:
                    result += s[i]
                    i += 1
            return result
                
        returnValue = rev(0).replace("(","").replace(")","")
        return returnValue
