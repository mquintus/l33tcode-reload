# 119 - Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currentRow = [1]
        
        for currentRowIndex in range(rowIndex):
            nextRow = [1]
            for position in range(1, len(currentRow)):
                nextRow.append(currentRow[position] + currentRow[position - 1])
            nextRow.append(1)
            currentRow = nextRow
        return currentRow
