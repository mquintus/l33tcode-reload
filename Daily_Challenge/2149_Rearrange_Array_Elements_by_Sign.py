# 2149 - Rearrange Array Elements by Sign
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        pos = [el for el in nums if el >= 0]
        neg = [el for el in nums if el < 0]
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
