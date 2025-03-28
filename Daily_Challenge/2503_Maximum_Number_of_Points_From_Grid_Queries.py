# 2503 - Maximum Number of Points From Grid Queries
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        thresholds = sorted(list(set(queries)))
        results = {}
        rows = len(grid)
        cols = len(grid[0])

        states = [(grid[0][0],0,0)]
        grid[0][0] = 10**6+1
        points = 0
        cells = 0
        for i, t in enumerate(thresholds):
            while states and t > states[0][0]:
                p, row, col = heapq.heappop(states)
                points += p
                cells += 1
                for row2, col2 in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if row2 >= 0 and col2 >= 0 and row2 < rows and col2 < cols:
                        heapq.heappush(states, (grid[row2][col2], row2, col2))
                        grid[row2][col2] = 10**6+1


            results[t] = cells

        return [results[i] for i in queries]

