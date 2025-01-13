# 3223 - Minimum Length of String After Operations
class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        for char in [chr(char) for char in range(ord('a'), ord('z') + 1)]:
            c = s.count(char) 
            if c == 0:
                continue
            if c % 2 == 0:
                l += 2
            else:
                l += 1
        return l
