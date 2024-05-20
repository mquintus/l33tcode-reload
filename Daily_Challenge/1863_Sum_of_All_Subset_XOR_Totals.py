# 1863 - Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xortotal = 0
        for length in range(1, len(nums)+1):
            for subset in itertools.combinations(nums, length):
                xor = reduce(operator.__xor__, subset)
                xortotal += xor
        return xortotal
