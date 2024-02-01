# 2966 - Divide Array Into Arrays With Max Difference
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n % 3 != 0:
            return []
        result = []
        for i in range(n // 3):
            result.append(nums[i*3:i*3+3])
            if nums[i*3+2] - nums[i*3] > k:
                return []
        return result
