# 3318 - Find X-Sum of All K-Long Subarrays I
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for start in range(len(nums) - k+1):
            total = 0
            freq = Counter(nums[start:start+k])
            freqitems = sorted([(f,v) for v,f in freq.items()])[-x:]
            for f,v in freqitems:
                total += f*v
            res.append(total)
        return res
