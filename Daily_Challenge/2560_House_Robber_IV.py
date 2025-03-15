# 2560 - House Robber IV
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # The question is basically to find the kth smallest number
        # but with a twist that none of the houses can be adjacent

        def is_possible(value): # return the biggest element in that range
            # a and b store the number of robbed houses
            a = 0
            b = 0
            maxel = 0
            for el in nums:
                if el > value:
                    el = 0
                else:
                    maxel = max(maxel, el)
                    el = 1
                c = max(a+el, b)
                a = b
                b = c
            if a < k and b < k:
                return 0
            return maxel

        items = list(sorted(set(nums)))
        start = 0
        end = len(items)
        while end > start:
            mid = (start+end)//2
            ip = is_possible(items[mid])
            #print(mid, ip)
            if ip == 0:
                start = mid + 1
            else:
                end = mid
        return items[start] if is_possible(items[start]) else items[end]
