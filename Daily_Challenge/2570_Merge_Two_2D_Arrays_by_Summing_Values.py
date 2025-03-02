# 2570 - Merge Two 2D Arrays by Summing Values
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c1 = {a:b for a,b in nums1}
        c2 = {a:b for a,b in nums2}

        for k,v in c2.items():
            if k not in c1:
                c1[k] = 0
            c1[k] += v
        
        result = list(c1.items())
        result.sort()

        return result
