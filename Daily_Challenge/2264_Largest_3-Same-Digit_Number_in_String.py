# 2264 - Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            target = f"{i}{i}{i}"
            if target in num:
                return target
        return ""
            
