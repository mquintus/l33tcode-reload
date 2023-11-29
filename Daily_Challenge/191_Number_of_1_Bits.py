# 191 - Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
