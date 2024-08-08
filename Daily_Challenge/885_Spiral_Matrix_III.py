# 885 - Spiral Matrix III
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r = rStart
        c = cStart
        li = []
        n = cols * rows
        
        d = 0
        nextstep = 1
        next2step = 2
        step = 1

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        while len(li) < n:
            if r < rows and r >= 0 and c < cols and c >= 0:
                li.append([r,c])
            c += dirs[d][0]
            r += dirs[d][1]
            step -= 1
            if step == 0:
                step = nextstep
                nextstep = next2step
                if step == nextstep: 
                    next2step += 1 
                d += 1
                d = d % 4

        return li
