# 200 - Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = set()

        def bfs(x, y):
            island.add((x,y,))
            nextStep = [(x,y,)]
            while nextStep:
                x,y = nextStep.pop()
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    px = x + dx
                    py = y + dy
                    if px >= 0 and py >= 0 and px < m and py < n:
                        t = (px, py)
                        if t not in island and grid[py][px] == "1":
                            nextStep.append(t)
                            island.add(t)

        islandcount = 0
        for py in range(n):
            for px in range(m):
                t = (px, py)
                if t in island:
                    continue
                if grid[py][px] == "1":
                    islandcount += 1
                    bfs(px, py)

        return islandcount
