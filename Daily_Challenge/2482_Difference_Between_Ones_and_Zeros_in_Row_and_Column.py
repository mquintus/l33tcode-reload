# 2482 - Difference Between Ones and Zeros in Row and Column
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        onesRow = []
        onesCol = []

        onesRow = [sum(row) for row in grid]
        onesCol = [sum([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]

        result = []
        for i in range(rows):
            new_row = []
            for j in range(cols):
                diff = onesRow[i] + onesCol[j] - (rows - onesRow[i]) - (cols - onesCol[j])
                new_row.append(diff)
            result.append(new_row)
        
        return result
