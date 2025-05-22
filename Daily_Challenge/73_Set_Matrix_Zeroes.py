# 73 - Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_active = [True for r in range(rows)]
        col_active = [True for c in range(cols)]

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0:
                    row_active[r] = False
                    col_active[c] = False

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if row_active[r] == False or col_active[c] == False:
                    matrix[r][c] = 0

