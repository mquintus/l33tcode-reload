# 1380 - Lucky Numbers in a Matrix
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        minPerRow = set()
        for row in matrix:
            minPerRow.add(min(row))
        for i in range(len(matrix[0])):
            col = [row[i] for row in matrix]
            maxPerCol = max(col)
            if maxPerCol in minPerRow:
                lucky.append(maxPerCol)
        return lucky
