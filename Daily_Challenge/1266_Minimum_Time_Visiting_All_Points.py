# 1266 - Minimum Time Visiting All Points
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        currx,curry = points[0]
        dist = 0
        for nextx, nexty in points[1:]:
            dist += max(abs(nextx-currx), abs(nexty-curry))
            currx,curry=nextx,nexty
        return dist
            
