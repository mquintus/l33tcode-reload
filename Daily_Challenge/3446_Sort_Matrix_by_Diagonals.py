# 3446 - Sort Matrix by Diagonals
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        
        def bubblesort(r,c,i,f_shouldSwap,hasSwapped):
            if r+i >= n-1 or c+i >= n-1:
                return hasSwapped 
            if f_shouldSwap(grid[r+i][c+i], grid[r+i+1][c+i+1]):
                grid[r+i][c+i], grid[r+i+1][c+i+1] = grid[r+i+1][c+i+1], grid[r+i][c+i]
                hasSwapped = True
            return bubblesort(r, c, i+1, f_shouldSwap,hasSwapped)

        for d in range(n):
            while bubblesort(d,0,0,lambda x,y: x<y, False): pass
            while bubblesort(0,1+d,0,lambda x,y: x>y, False): pass
        
        return grid
