# 717 - 1-bit and 2-bit Characters
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0 
        while i < n:
            if i == n - 1:
                return True
            if bits[i] == 0:
                i += 1
            if bits[i] == 1:
                i += 2
        return False
