# 118 - Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        rows = [[1],[1,1]]
        if numRows == 2:
            return rows
        for i in range(2,numRows):
            row = rows[-1]
            nextRow = [1]
            for j in range(1,len(row)):
                nextRow.append(row[j] + row[j-1])
            nextRow.append(1)
            rows.append(nextRow)
        return rows
