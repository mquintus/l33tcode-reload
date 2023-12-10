# 867 - Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        # Matrix is higher than wide
        if m < n:
            for i in range(n):
                for addup in range(n - m):
                    matrix[i].append(None)

        # Matrix is wider than high
        if n < m:
            for addup in range(n, m):
                matrix.append([None] * m)

        l = max(m,n)
        for i in range(l):
            for j in range(i, l):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        return [row[:n] for row in matrix[:m]]
