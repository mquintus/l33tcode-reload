# 2290 - Minimum Obstacle Removal to Reach Corner
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dist = m-1 + n-1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False]*n for _ in range(m)]
        states = deque()
        states.append((0,0,0))
        while states:
            remov, row, col = states.popleft()

            for dr,dc in directions:
                dr += row
                dc += col
                if not (dr >= 0 and dc >= 0 and dr < m and dc < n):
                    continue
                if visited[dr][dc]:
                    continue
                newstate = (remov+grid[dr][dc],dr, dc)
                if grid[dr][dc] == 1:
                    states.append(newstate)
                else:
                    states.appendleft(newstate)
                # Mark cell as "visited" as soon as it's appended
                visited[dr][dc] = True
                if dr == m-1 and dc == n-1:
                    return remov

                
