# 1750 - Minimum Length of String After Deleting Similar Ends
class Solution:
    def minimumLength(self, s: str) -> int:
        p0 = 0
        p1 = len(s) - 1
        n = len(s)
        while p0 < p1 and s[p0] == s[p1]:
            prev = s[p0]
            while p0 < n and p1 >= p0 and s[p0] == prev:
                p0 += 1
            prev = s[p1]
            while p1 >= 0 and p1 >= p0 and s[p1] == prev:
                p1 -= 1
        return p1 - p0 + 1
