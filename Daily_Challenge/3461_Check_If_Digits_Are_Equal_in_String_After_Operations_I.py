# 3461 - Check If Digits Are Equal in String After Operations I
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(d) for d in s]
        for m in range(len(s)-1, 1, -1):
            for i in range(m):
                s[i] += s[i+1] 
                s[i] %= 10
        return s[0] == s[1]
