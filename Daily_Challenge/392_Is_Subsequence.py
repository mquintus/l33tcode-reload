# 392 - Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
            
        pointer1 = 0
        for pointer2 in range(len(t)):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
            if pointer1 == len(s):
                return True
        return False
