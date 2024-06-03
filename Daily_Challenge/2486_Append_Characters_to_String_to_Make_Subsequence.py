# 2486 - Append Characters to String to Make Subsequence
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        n = len(t)
        for char in s:
            if t[p] == char:
                p += 1
            if p == n:
                break
        return n - p
