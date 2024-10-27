# 1277 - Count Square Submatrices with All Ones
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        targets = []
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                for tr, tc in [(row-1,col-1),(row, col-1),(row-1,col),(row,col)]:
                    if matrix[tr][tc] == 0:
                        break
                else:
                    matrix[tr][tc] += 1
                    targets.append((tr,tc))
        while targets:
            row, col = targets.pop(0)
            for tr, tc in [(row-1,col-1),(row, col-1),(row-1,col)]:
                if matrix[tr][tc] < matrix[row][col]:
                    break
            else:
                matrix[row][col] += 1
                targets.append((row,col))
        #print(matrix)
        return sum([sum(row) for row in matrix])
                
