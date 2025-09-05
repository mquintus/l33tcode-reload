# 2749 - Minimum Operations to Make the Integer Zero
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        remainder = 1

        #if num1.bit_count() == 0:
        #    return 0

        times = 0
        while True:
            times += 1
            num1 -= num2
            if num1 < times: return -1
            if num1.bit_count() == times: # e.g. 24 = 16+8  where times = 2
                return times
            if num1.bit_count() < times: # e.g. 32 = 16+8+8  where times = 3 is the same as 
                return times  # 16+16 is the same as 32  meaning that it is always possible to decompose
                # any power of two by more, smaller powers of two 
                # therefore if times>bitcount, with times = 3 instead of subtrating 32 once you can subtract 16,8,8

            
