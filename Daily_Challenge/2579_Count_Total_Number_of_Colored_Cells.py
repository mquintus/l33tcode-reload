# 2579 - Count Total Number of Colored Cells
class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return 1 + 4 * (n-1) * (n) // 2
