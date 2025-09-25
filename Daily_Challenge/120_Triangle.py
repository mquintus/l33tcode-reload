# 120 - Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i-1][max(0,j-1):j+1])
        return min(triangle[-1])
