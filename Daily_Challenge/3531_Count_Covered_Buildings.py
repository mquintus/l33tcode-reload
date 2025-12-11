# 3531 - Count Covered Buildings
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = {}
        cols = {}
        for r,c in buildings:
            if r not in rows: rows[r] = [n+1,0]
            if c not in cols: cols[c] = [n+1,0]

            rows[r] = [min(rows[r][0], c), max(rows[r][1], c)]
            cols[c] = [min(cols[c][0], r), max(cols[c][1], r)]
        
        total = 0
        for r,c in buildings:
            if r == 1 or r == n or c == 1 or c == n: continue

            if r < cols[c][1] and cols[c][0] < r and c < rows[r][1] and rows[r][0] < c: total += 1


        return total
