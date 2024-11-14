# 2064 - Minimized Maximum of Products Distributed to Any Store
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities) == n:
            return max(quantities)

        def trySolution(s):
            slots = 0
            for q in quantities:
                slots += math.ceil(q / s)
            return slots

        low = 1
        high = max(quantities) + 1
        while low < high:
            mid = (low + high)//2
            slots = trySolution(mid)
            #print(mid, slots)
            if slots > n:
                low = mid + 1
            elif slots < n:
                if mid == 1 or trySolution(mid-1) > n:
                    break
                high = mid
            else:
                if trySolution(mid-1) == n:
                    high = mid
                else:
                    break
        return mid



                

