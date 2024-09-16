# 539 - Minimum Time Difference
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        def convert(s):
            return int(s[:2])*60 + int(s[-2:])
        timePoints = sorted(list(map(convert, timePoints)))
        smallest_difference = (timePoints[0] - timePoints[-1])%(1440)
        for i,tp in enumerate(timePoints[1:]):
            d = tp - timePoints[i]
            smallest_difference = min(smallest_difference, d)
            if smallest_difference == 0:
                return 0
        return smallest_difference
