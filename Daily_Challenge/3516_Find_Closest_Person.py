# 3516 - Find Closest Person
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(z-x)
        dist2 = abs(z-y)
        if dist1 == dist2 : return 0
        if dist1 < dist2 : return 1
        if dist1 > dist2 : return 2
