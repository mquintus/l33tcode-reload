# 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        states = deque()
        states.append((0,0,0))
        while states:
            cost, x, y = states.popleft()
            #print("State",cost, x, y)
            if x == n-1 and y == m-1:
                return cost

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for i, (dx,dy) in enumerate(directions):
                if grid[x][y] == 0:
                    continue

                nx, ny = x+dx, y+dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if grid[nx][ny] == 0:
                    continue
                
                if grid[x][y] == i + 1:
                    dcost = cost
                else:
                    dcost = cost + 1

                if cost == dcost:
                    if nx == n-1 and ny == m-1:
                        return cost
                    states.appendleft((dcost,nx,ny))
                else:
                    states.append((dcost,nx,ny))
            grid[x][y] = 0
