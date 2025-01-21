# 2017 - Grid Game
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        postfixA = sum(grid[0][1:])
        prefixB = 0

        bestSolutionB = max(postfixA, prefixB)
        for i in range(1, len(grid[0])):
            postfixA -= grid[0][i]
            prefixB += grid[1][i-1]

            bestSolutionTempB = max(postfixA, prefixB)
            if bestSolutionB > bestSolutionTempB:
                bestSolutionB = bestSolutionTempB
        
        return bestSolutionB
