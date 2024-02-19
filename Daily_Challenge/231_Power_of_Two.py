# 231 - Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: 
            return False
        found = False
        for bit in "{0:b}".format(n):
            if bit == '1':
                if found: 
                    return False
                found = True
        return found
