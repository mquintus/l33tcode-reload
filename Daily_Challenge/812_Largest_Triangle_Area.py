# 812 - Largest Triangle Area
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = -1
        for i, (x1,y1) in enumerate(points):
            for j, (x2,y2) in enumerate(points):
                if j <= i: continue
                for k, (x3,y3) in enumerate(points):
                    if k <= j: continue
                    area = max(area, 0.5*abs(
                          x1*(y2-y3)
                        + x2*(y3-y1)
                        + x3*(y1-y2)
                    ))
        return area
