# 1905 - Count Sub Islands
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        def findIsland(col, row) -> set():
            #print('-'*10)
            queue = deque([(col, row)])
            grid2[row][col] = 0
            isValid = 1
            while queue:
                col, row = queue.popleft()
                if grid1[row][col] == 0:
                    isValid = 0
                for dc,dr in [[0,-1],[-1,0],[1,0],[0,1]]:
                    if col+dc >= 0 and col+dc < n and row+dr >= 0 and row+dr < m and grid2[row+dr][col+dc] == 1:
                        queue.append((col+dc,row+dr))
                        grid2[row+dr][col+dc] = 0    
                #print(col, row, isValid)
            return isValid
        
        validIslands = 0
        for col in range(n):
            for row in range(m):
                if grid2[row][col] == 1:
                    validIslands += findIsland(col, row)
            
        return validIslands
