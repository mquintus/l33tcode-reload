# 2661 - First Completely Painted Row or Column
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        index = [[] for _ in range(rows*cols + 1)]
        for r in range(rows):
            for c in range(cols):
                i = r + c * cols
                index[mat[r][c]] = (r,c)
        paintedRows = [0 for _ in range(rows)]
        paintedCols = [0 for _ in range(cols)]
        for i in range(len(arr)):
            el = arr[i]
            r = index[el][0]
            c = index[el][1]
            paintedRows[r] += 1
            paintedCols[c] += 1
            if paintedRows[r] == cols or paintedCols[c] == rows: return i


