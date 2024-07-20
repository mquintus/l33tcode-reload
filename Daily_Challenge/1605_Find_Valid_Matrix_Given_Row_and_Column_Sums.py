# 1605 - Find Valid Matrix Given Row and Column Sums
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0] * m for _ in range(n)]

        rowId = 0
        colId = 0
        while rowId < n and colId < m:
            val = min([rowSum[rowId], colSum[colId]]) 
            rowSum[rowId] -= val
            colSum[colId] -= val
            matrix[rowId][colId] = val
            if rowSum[rowId] == 0:
                rowId += 1
            if colSum[colId] == 0:
                colId += 1
        return matrix
