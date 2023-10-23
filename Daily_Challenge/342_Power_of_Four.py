# 342 - Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        mask = 0b01010101010101010101010101010101

        if mask | n != mask:
            return False

        # The number is the sum of powers of four.
        # But how do we check that only one of the bits is set?
        #
        # This part is funny 
        #
        # Let's assume there is only 1 bit set.
        # If we subtract the number 1, the binary representation 
        # of
        # 10000000000000000
        # will turn into
        # 01111111111111111
        #
        # So we can AND (&) and it will be 0
        #
        # but if two bits are set ...
        # 10001000000000000
        # subtracting 1 will lead to
        # 10000111111111111
        # and if we AND that, it is not 0

        if n & (n-1) == 0:
            return True
        return False



