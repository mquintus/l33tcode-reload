# 238 - Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]
        right = [1]
        for el in nums:
            left.append(left[-1] * el)
        for el in nums[::-1]:
            right.append(right[-1] * el)
        result = [right[n-1]]
        for i in range(n-2):
            result.append(right[n-2-i] * left[i+1])
        result.append(left[n-1])
        return result
