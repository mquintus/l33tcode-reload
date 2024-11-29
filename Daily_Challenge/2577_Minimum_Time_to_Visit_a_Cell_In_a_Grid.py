# 2577 - Minimum Time to Visit a Cell In a Grid
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        visited = [[False] * n for _ in range(m)]
        
        states = [(0,0,0)]
        while states:
            #print(states)
            time,r,c = heapq.heappop(states)
            if r == m-1 and c == n-1:
                #print("Reached",r,c,"at",time)
                return time
            #print(r,c, '(',grid[r][c],')')
            time += 1
            prevtime = time
            for dr,dc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                if dr < 0 or dr >= m or dc < 0 or dc >= n:
                    continue
                #print(f"Looking at ({dr},{dc}) value {grid[dr][dc]}")
                if not visited[dr][dc]:
                    visited[dr][dc] = True
                    if grid[dr][dc] <= prevtime:
                        #print(f"Adding {(prevtime,dr,dc)}")
                        heapq.heappush(states, (prevtime,dr,dc))
                    else:
                        time = prevtime + ((grid[dr][dc] - prevtime + 1) // 2) * 2
                        #print(dr,dc,'=',grid[dr][dc],"to", time, f"now: {prevtime}")
                        heapq.heappush(states, (time,dr,dc))

        return -1
        
            
