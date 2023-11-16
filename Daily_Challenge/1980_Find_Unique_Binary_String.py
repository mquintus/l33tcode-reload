# 1980 - Find Unique Binary String
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = 2**len(nums)
        resultformat = "{:0"+str(len(nums))+"b}"
        matches = {}
        for num in nums:
            matches[int(num, 2)] = 1
        
        for i in range(n):
            if i not in matches:
                return resultformat.format(i)
