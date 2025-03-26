# 2033 - Minimum Operations to Make a Uni-Value Grid
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        allNumbers = []
        for row in grid:
            allNumbers.extend(row)
        allNumbers.sort()
        
        n = len(allNumbers)
        pivot = n // 2
        pivotEl = allNumbers[pivot]


        operations = 0
        for el in allNumbers:
            distance = abs(pivotEl - el)
            if distance % x != 0:
                return -1
            else:
                operations += (distance // x)

        return operations
