# 3000 - Maximum Area of Longest Diagonal Rectangle
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        for i in range(len(dimensions)):
            x,y = dimensions[i]
            dimensions[i] = (x**2+y**2, x*y)
        dimensions.sort()
        return dimensions[-1][1]
