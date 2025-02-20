# 1980 - Find Unique Binary String
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        unequal = []
        for i, num in enumerate(nums):
            unequal.append(str(1-int(num[i])))
        return "".join(unequal)
