# 476 - Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        base = 2
        while base <= num:
            base *= 2
        return (base-1)-num
