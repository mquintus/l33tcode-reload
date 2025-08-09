# 231 - Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        while n > 0:
            if n > 1 and n&1: return False
            n //= 2
        return True
