# 1765 - Map of Highest Peak
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        states = deque()
        for r, row in enumerate(isWater):
            for c, cell in enumerate(row):
                if cell == 1:
                    states.append((0,r,c))
                    isWater[r][c] = 0
                else:
                    isWater[r][c] = -1

        
        while states:
            h,r,c = states.popleft()
            isWater[r][c] = h

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if isWater[nr][nc] >= 0: 
                    continue
                
                states.append((h+1, nr, nc))
                isWater[nr][nc] = h+1

        return isWater


