# 260 - Single Number III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        globalXOR = reduce(operator.__xor__, nums)
        p = 1
        smallestBit = p & globalXOR
        while smallestBit == 0:
            p <<= 1
            smallestBit = p & globalXOR

        groupAxor = 0
        groupBxor = 0
        for el in nums:
            if el & p:
                groupAxor ^= el
            else:
                groupBxor ^= el
        return [groupAxor, groupBxor]
