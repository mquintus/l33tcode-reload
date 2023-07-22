class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def number_of_rounds(k):
            rounds = 0
            for p in piles:
                rounds += ceil(p / k)
            return rounds

        start = 1
        end = max(piles) + 1
        min_val = end
        while start < end:
            mid = start + (end - start) // 2
            if number_of_rounds(mid) <= h:
                min_val = mid
                end = mid
                continue
            start = mid + 1

        return min_val

# [3,6,7,11]
# 8
# [30,11,23,4,20]
# 5
# [30,11,23,4,20]
# 6
# [805306368,805306368,805306368]
# 1000000000
# [1,1,1,999999999]
# 10
# [1,2,3,4,5]
# 1000000000
# [1000000000]
# 2
# [312884470]
# 312884469
