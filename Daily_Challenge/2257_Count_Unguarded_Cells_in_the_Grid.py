# 2257 - Count Unguarded Cells in the Grid
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] *n for _ in range(m)] 
        for row, col in guards:
            grid[row][col] = 2
        for row, col in walls:
            grid[row][col] = 3

        #print(grid)

        counter = 0
        for g_row, g_col in guards:
            for d_row, d_col in [(0,1),(1,0),(0,-1),(-1,0)]:
                row = g_row
                col = g_col
                row += d_row
                col += d_col
                while row >= 0 and row < m and col >= 0 and col < n:
                    if grid[row][col] < 2:
                        if grid[row][col] == 0:
                            counter += 1
                            grid[row][col] = 1
                        row += d_row
                        col += d_col
                    else:
                        break
        #print(f"{n*m} - {len(guards)} - {len(walls)} - {counter}")
        return n*m - len(guards) - len(walls) - counter
