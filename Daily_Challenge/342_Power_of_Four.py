# 342 - Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        return (n & n - 1) == 0 and (n - 1) % 3 == 0
