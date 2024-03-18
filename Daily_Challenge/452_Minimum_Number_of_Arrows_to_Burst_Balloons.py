# 452 - Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count = 0
        end = float("-inf")
        for a, b in points:
            if end < a:
                count += 1
                end = b
        return count
