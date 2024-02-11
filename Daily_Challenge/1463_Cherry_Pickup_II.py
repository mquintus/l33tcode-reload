# 1463 - Cherry Pickup II
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0 for _ in range(m)]  for _ in range(m)]  for _ in range(n)]
        dp[0][0][m-1] = grid[0][0] + grid[0][m-1]
        #print(dp)

        maxPoints = -1
        for row in range(0, n):

            for c1 in range(0, min(m, row+1)):
                for c2 in range(max(0, m-row-1), m):
                    if c1 >= c2:
                        continue
                    if row == n - 1:
                        maxPoints = max(maxPoints, dp[row][c1][c2])
                        continue

                    prevPoints = 0
                    for next_c1 in range(max(0, c1 - 1), min(m, c1 + 2)):
                        for next_c2 in range(max(0, c2 - 1), min(m, c2 + 2)):
                            if next_c1 >= next_c2:
                                continue

                            gridPoints = grid[row+1][next_c1] + grid[row+1][next_c2]
                            prevPoints = dp[row][c1][c2]
                            dp[row+1][next_c1][next_c2] = max(dp[row+1][next_c1][next_c2], gridPoints + prevPoints)

        return maxPoints
