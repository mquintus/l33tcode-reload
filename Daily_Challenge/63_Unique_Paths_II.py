class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[h-1][w-1] == 1:
            return 0

        obstacleGrid[h-1][w-1] = -1
        
        for y in range(h-1, -1, -1):
            rowsum = 0
            for x in range(w-1, -1, -1):
                rowsum += 1
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                elif obstacleGrid[y][x] == -1:
                    obstacleGrid[y][x] = 1
                else:
                    if x < w - 1:
                        obstacleGrid[y][x] += obstacleGrid[y][x + 1] 
                    if y < h - 1:
                        obstacleGrid[y][x] += obstacleGrid[y+1][x]
            if rowsum == 0:
                return 0

        return obstacleGrid[0][0]
