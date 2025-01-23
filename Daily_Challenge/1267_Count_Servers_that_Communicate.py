# 1267 - Count Servers that Communicate
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        validRow = [False] * 250
        validCol = [False] * 250
        prevRow = [-1] * 250
        counterRow = [False] * 250
        for r in range(rows):
            counter = False
            prev = -1
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                if counterRow[c]:
                    validCol[c] = True
                    validRow[r] = True
                    validRow[prevRow[c]] = True
                counterRow[c] = True
                prevRow[c] = r

                if validRow[r]:
                    validCol[c] = True
                    continue

                if counter == False:
                    counter = True
                    prev = c
                    continue

                if counter == True:
                    validRow[r] = True
                    validCol[c] = True
                    validCol[prev] = True

        result = 0
        for r in range(rows):
            if not validRow[r]:
                continue
            result += sum(grid[r])
        return result
