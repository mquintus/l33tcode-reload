# 350 - Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        C2 = Counter(nums2)
        for k,v in Counter(nums1).items():
            if k not in C2:
                continue
            v = min(v, C2[k])
            if v > 0:
                result += [k]*v
        return result
