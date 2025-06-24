# 2200 - Find All K-Distant Indices in an Array
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        distances = [n] * n
        last_match = -1
        for i, el in enumerate(nums):
            if el == key: 
                last_match = i
            if last_match != -1:
                distances[i] = min(distances[i], i - last_match)
        if last_match == -1:
            return []
        
        last_match = -1
        for i in range(n-1,-1,-1):
            el = nums[i]
            if el == key: 
                last_match = i
            if last_match != -1:
                distances[i] = min(distances[i], last_match - i)
        
        result = []
        for i,dist in enumerate(distances):
            if dist <= k:
                result.append(i)
        return result
        

