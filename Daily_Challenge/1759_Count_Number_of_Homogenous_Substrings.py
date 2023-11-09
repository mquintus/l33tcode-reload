# 1759 - Count Number of Homogenous Substrings
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0

        prev = "!"
        length = 0
        for char in s:
            if char != prev:
                dp += ((length + 1) * length) // 2
                length = 0
                prev = char
            length += 1
        dp += ((length + 1) * length) // 2
        dp %= MOD

        return dp
            
