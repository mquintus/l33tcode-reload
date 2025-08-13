# 326 - Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        b = 1
        for i in range(n):
            if b > n: break
            if b == n: return True
            b *= 3
        return False
