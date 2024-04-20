# 1992 - Find All Groups of Farmland
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        grid = land
        n = len(grid)
        m = len(grid[0])
        island = set()

        def bfs(x, y):
            startx,starty=x,y
            endx,endy=x,y
            island.add((x,y,))
            nextStep = [(x,y,)]
            while nextStep:
                x,y = nextStep.pop()
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    px = x + dx
                    py = y + dy
                    if px >= 0 and py >= 0 and px < m and py < n:
                        t = (px, py)
                        if t not in island and grid[py][px] == 1:
                            nextStep.append(t)
                            island.add(t)
                            endx=max(endx,px)
                            endy=max(endy,py)
            islandcoords.append([starty,startx,endy,endx])

        islandcoords = []
        for py in range(n):
            for px in range(m):
                t = (px, py)
                if t in island:
                    continue
                if grid[py][px] == 1:
                    bfs(px, py)

        return islandcoords
