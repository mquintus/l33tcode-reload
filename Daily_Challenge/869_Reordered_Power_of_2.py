# 869 - Reordered Power of 2
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        strn = str(n)
        availableDigits = Counter(strn)
        b = 1
        for i in range(32):
            strb = str(b)
            b *= 2
            if len(strb) > len(strn):
                return False
            if len(strb) < len(strn):
                continue
            necDigits = Counter(strb)
            if availableDigits == necDigits:
                return True
            
        return False
        
        
