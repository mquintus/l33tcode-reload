# 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        leftCount = sum([1 for el in nums1 if el == 0])
        leftSum = sum(nums1)
        rightCount = sum([1 for el in nums2 if el == 0])
        rightSum = sum(nums2)
        minSumLeft = leftCount + leftSum
        minSumRight = rightCount + rightSum
        if leftCount == 0 and minSumRight > minSumLeft: return -1
        if rightCount == 0 and minSumLeft > minSumRight: return -1
        return max(minSumLeft, minSumRight)
