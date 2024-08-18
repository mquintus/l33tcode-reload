# 1937 - Maximum Number of Points with Cost
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        nextarr = points[0]
        rightarr = points[0]
        currarr = points[0]
        n = len(points)
        m = len(points[0])
        for rowid in range(1, n):
            for target in range(1,m):
                val = nextarr[target-1] - 1
                bestval = max(val, currarr[target])
                nextarr[target] = bestval
                
            for target in range(m-2,-1,-1):
                val = rightarr[target+1] - 1
                bestval = max(val, currarr[target])
                rightarr[target] = bestval

            for target in range(m):
                currarr[target] = points[rowid][target] + max(nextarr[target], rightarr[target])



        return max(currarr)

