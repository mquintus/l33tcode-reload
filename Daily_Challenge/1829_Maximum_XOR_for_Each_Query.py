# 1829 - Maximum XOR for Each Query
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        something = 2**maximumBit-1
        xorall = 0
        for el in nums:
            xorall = xorall ^ el
        xorall ^= something

        solution = []
        solution.append(xorall)
        for el in nums[:0:-1]:
            xorall ^= el
            solution.append(xorall)
        
        return solution
