class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        This sounds like a two-pointer problem.
        Each round, we iterate on of the pointers (the one whose follower is smaller) and add the pair that both pointers are pointing to.
        '''
