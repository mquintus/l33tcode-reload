class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        This sounds like a two-pointer problem.
        Each round, we iterate on of the pointers (the one whose follower is smaller) and add the pair that both pointers are pointing to.
        '''
        pairs = []
        p = [0, 0]
        for i in range(k):
            print(p, len(nums1), len(nums2), k)
            pairs.append([nums1[p[0]], nums2[p[1]]])

            if len(nums1) > p[0] + 1 and (len(nums2) == p[1] + 1 or nums1[p[0] + 1] < nums2[p[1] + 1]):
                p[0] += 1
                p[1] = 0
            elif len(nums2) > p[1] + 1:
                p[0] = 0
                p[1] += 1
            else:
                break
        return pairs
        
