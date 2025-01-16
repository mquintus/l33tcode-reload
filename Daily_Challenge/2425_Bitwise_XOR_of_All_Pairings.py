# 2425 - Bitwise XOR of All Pairings
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums2) % 2 == 1:
            for el in nums1:
                result ^= el
        if len(nums1) % 2 == 1:
            for el in nums2:
                result ^= el
        return result

