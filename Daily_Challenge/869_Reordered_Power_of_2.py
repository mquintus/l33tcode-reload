# 869 - Reordered Power of 2
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        availableDigits = Counter(str(n))
        b = 1
        for i in range(32):
            necDigits = Counter(str(b))
            b *= 2
            if availableDigits == necDigits:
                return True
        return False
        
