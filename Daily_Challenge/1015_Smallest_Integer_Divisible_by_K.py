# 1015 - Smallest Integer Divisible by K
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1

        while n < k:
            n *= 10
            n += 1

        size = len(str(n))
        counter = k + 1
        while counter > 0:
            if n % k == 0:
                return size
            else:
                counter -= 1
                size += 1
            n *= 10
            n += 1
            n %= k
        return -1 
            
