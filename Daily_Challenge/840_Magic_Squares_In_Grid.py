# 840 - Magic Squares In Grid
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for startrow in range(0, len(grid)-2):
            for startcol in range(0, len(grid[0])-2):
                isgood = True
                seen = [False] * 15
                for row in range(startrow, startrow+3):
                    for col in range(startcol, startcol+3):
                        number = grid[row][col]
                        if number < 1 or number > 9 or seen[number-1] == True:
                            isgood = False
                            break
                        seen[number-1] = True
                    if not isgood: break
                if not isgood: continue
                for row in range(startrow, startrow+3):
                    if not isgood or sum(grid[row][startcol:startcol+3]) != 15:
                        isgood = False
                        break
                for col in range(startcol, startcol+3):
                    if not isgood or sum([grid[startrow][col],grid[startrow+1][col],grid[startrow+2][col]]) != 15:
                        isgood = False
                        break
                #diagonals
                if not isgood or sum([grid[startrow][startcol],grid[startrow+1][startcol+1],grid[startrow+2][startcol+2]]) != 15:
                    isgood = False
                    continue
                if not isgood or sum([grid[startrow][startcol+2],grid[startrow+1][startcol+1],grid[startrow+2][startcol]]) != 15:
                    isgood = False
                    continue
                if isgood:
                    count += 1
        return count 
