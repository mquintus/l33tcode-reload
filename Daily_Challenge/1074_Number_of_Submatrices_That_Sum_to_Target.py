# 1074 - Number of Submatrices That Sum to Target
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        #dp[y][x][h][w]
        #100 100 100 100
        # 100_000_000
        n = len(matrix)
        m = len(matrix[0])
        dp = [[[[float('nan') for _ in range(m-x)] for _ in range(n-y)] for x in range(m)] for y in range(n)]
        counter = 0

        #print(dp)
        for h in range(0,n):
            for w in range(0,m):
                #print("w,h",w,h)
                for y in range(0,n-h):
                    for x in range(0,m-w):
                        #print("x,y",x,y)
                        positionvalue = matrix[y+h][x+w]
                        #print("position", x+w, y+h, 'value', positionvalue)
                        #print('pre', x,y,w,h, dp[y][x][h][w])
                        dp[y][x][h][w] = positionvalue
                        #print(dp[y][x][h][w])
                        if w > 0 and h > 0:
                            #print('Adding cuadro', dp[y][x][h][w])
                            dp[y][x][h][w] += dp[y][x][h-1][w-1]
                        if h > 0:
                            #print('Adding row', y, x+w,h,0, dp[y][x+w][h][0], 'to', dp[y][x][h][w])
                            dp[y][x][h][w] += dp[y][x+w][h-1][0]
                            #print('so', dp[y][x][h][w])
                        if w > 0:
                            #print('Adding part row', dp[y+h][x][0][w])
                            dp[y][x][h][w] += dp[y+h][x][0][w-1]
                        if target == dp[y][x][h][w]:
                            counter += 1
                            #print('Match',x,y,w,h)
                        #print("Writing dp[y][x][h][w]", y,x,h,w, dp[y][x][h][w])

                        #print(dp[y][x])
                        #print(dp[y][x][h][w])
        #print(dp)
        return counter
