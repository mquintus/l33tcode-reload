class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]
            if a < b:
                i += 1
            elif b < a:
                j += 1
            elif b == a:
                return a
        return -1
