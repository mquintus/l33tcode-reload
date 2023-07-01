class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0 for x in range(col)] for y in range(row)]
        visited_grid = [[-1 for x in range(col)] for y in range(row)]
        for day, cell in enumerate(cells):
            grid[cell[0] - 1][cell[1] - 1] = day + 1

        def dfs(y, x, day):
            visited_grid[y][x] = day
            if y == row - 1:
                return [[y+1,x+1]]

            path = []
            for ny, nx in [(y+1, x), (y, x+1), (y, x-1), (y-1, x)]:
                if 0<=nx<col and 0<=ny<row and visited_grid[ny][nx] != day:
                    if grid[ny][nx] > day:
                        visited_grid[ny][nx] = day
                        path = dfs(ny, nx, day)

                if path != -1 and path != []:
                    break
            if path == -1 or path == []:
                return -1
            return [[y+1,x+1], *path]

        path = -1
        old_path = -1
        first_day = col - 2
        last_day = (col-1)*row + 1
        mid = -1
        while first_day < last_day:
            mid = first_day + (last_day - first_day) // 2
            x = 0
            path = -1
            while x < col:
                if grid[0][x] > mid:
                    path = dfs(0, x, mid)
                    x+=2
                else:
                    x+=1
                    
                if path != -1 and path != []:
                    break

            if path == -1 or path == []:
                last_day = mid
            else:
                first_day = mid + 1
                old_path = path
        if path == -1:
            mid -= 1
        return mid 
