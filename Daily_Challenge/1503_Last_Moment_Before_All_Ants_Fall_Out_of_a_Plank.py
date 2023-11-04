# 1503 - Last Moment Before All Ants Fall Out of a Plank
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        times = [*left, *[n - r for r in right]]
        return max(times)
