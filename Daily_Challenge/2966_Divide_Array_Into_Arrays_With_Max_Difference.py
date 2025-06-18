# 2966 - Divide Array Into Arrays With Max Difference
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k: return []
            result.append(nums[i:i+3])
        return result
