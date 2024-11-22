# 1072 - Flip Columns For Maximum Number of Equal Rows
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = {}
        mp = 0
        for row in matrix:
            prev = row[0]
            pattern = []
            for el in row:
                pattern.append(el == prev)
                prev = el
            pattern = tuple(pattern)
            if pattern not in patterns:
                patterns[pattern] = 0
            patterns[pattern] += 1
            mp = max(mp,patterns[pattern])
        return mp

        
