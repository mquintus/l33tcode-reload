import functools
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        options = [(-1,-2), (-2,-1), (1,-2), (2,-1), (1,2), (2,1), (-1,2), (-2,1)]

        @cache
        def solve(n: int, k: int, row: int, column: int) -> float:
            if row < 0 or column < 0 or row >= n or column >= n:
                return 0
            if k == 0:
                return 1

            res = 0
            for o in options:
                res += solve(n, k - 1, row+o[0], column+o[1])
            return res / 8
        
        return solve(n, k, row, column)
