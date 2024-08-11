# 959 - Regions Cut By Slashes
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])

        edges={}
        for row in range(n):
            for col in range(m):
                for p in range(0,2):
                    edges[(row,col,p)] = set()

        def connect_left(row, col):
            if col == 0:
                return
            nonlocal edges
            edges[(row,col,0)].add((row,col-1,1))
            edges[(row,col-1,1)].add((row,col,0))

        def connect_upwards(row, col, p):
            if row == 0:
                return
            nonlocal edges
            if grid[row-1][col] in ["/", " "]:                
                edges[(row,col,p)].add((row-1,col,1))
                edges[(row-1,col,1)].add((row,col,p))
            if grid[row-1][col] in ["\\", " "]:
                edges[(row,col,p)].add((row-1,col,0))
                edges[(row-1,col,0)].add((row,col,p))

        areas = []
        for row in range(n):
            for col in range(m):
                connect_left(row,col)
                if grid[row][col] == " ":
                    edges[(row,col,0)].add((row,col,1))
                    edges[(row,col,1)].add((row,col,0))
                    connect_upwards(row,col,0)
                    connect_upwards(row,col,1)
                elif grid[row][col] == "\\":
                    connect_upwards(row,col,1)
                elif grid[row][col] == "/":
                    connect_upwards(row,col,0)

        visited = set()
        def dfs(row, col, p):
            nonlocal visited
            for nrow in range(max(0, row-1),min(n,row+2)):
                for ncol in range(max(0, col-1),min(m,col+2)):
                    for np in [0,1]:
                        if (nrow, ncol, np) in edges[row,col,p]:
                            if not (nrow, ncol, np) in visited:
                                visited.add((nrow, ncol, np))
                                dfs(nrow, ncol, np)

        counter = 0
        for row in range(n):
            for col in range(m):
                for p in range(0,2):
                    if (row, col, p) not in visited:
                        counter += 1
                        #print(row, col, p)
                        dfs(row, col, p)

        return counter
