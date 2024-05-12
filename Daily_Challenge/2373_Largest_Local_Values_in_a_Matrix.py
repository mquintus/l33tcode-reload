# 2373 - Largest Local Values in a Matrix
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxgrid = []
        for row_i in range(1, n-1):
            maxgrid.append([])
            for cell_i in range(1, n-1):
                maxval = max(
                    [max(
                        [grid[row_j][cell_j] for cell_j in [cell_i - 1, cell_i, cell_i + 1]]) for row_j in [row_i - 1, row_i, row_i + 1]
                       ])
                maxgrid[-1].append(maxval)
        return maxgrid
