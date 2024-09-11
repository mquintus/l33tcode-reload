# 2220 - Minimum Bit Flips to Convert Number
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return int.bit_count(start^goal)
