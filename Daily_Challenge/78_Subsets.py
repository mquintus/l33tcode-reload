# 78 - Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = set([()])
        for length in range(len(nums)+1):
            subsets = itertools.combinations(nums, length)
            for s in subsets:
                all_subsets.add(tuple(s))
        return [list(s) for s in all_subsets]
