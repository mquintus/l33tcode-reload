class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        This sounds like a two-pointer problem.
        Each round, we iterate on of the pointers (the one whose follower is smaller) and add the pair that both pointers are pointing to.
        '''
        hashmap = {}
        pairs = []
        p = [0, 0]
        reset = [{}, {}]
        i = 0
        while i < k * 2:
            #print(p)
            pairs.append([nums1[p[0]], nums2[p[1]]])
            #print(pairs)
            i += 1
            reset[1][p[0]] = p[1] + 1
            reset[0][p[1]] = p[0] + 1

            if len(nums1) == p[0] + 1 and len(nums2) == p[1] + 1:
                break

            r0 = 0
            if p[1]+1 in reset[0]:
                r0 = reset[0][p[1]+1]
            r1 = 0
            if p[0]+1 in reset[1]:
                r1 = reset[1][p[0]+1]
            if len(nums2) <= p[1] + 1 or len(nums1) > p[0] + 1 and nums2[r1] + nums1[p[0] + 1] < nums1[r0] + nums2[p[1] + 1]:
                p[1] = r1 
                p[0] += 1
            elif len(nums2) > p[1] + 1:
                p[0] = r0
                p[1] += 1
            else:
                break
        # Since the sorting isn't accepted: Sort again at the end
        #
        return sorted(pairs, key=lambda el: el[0] + el[1] + el[1] / 1000000)[:k]
