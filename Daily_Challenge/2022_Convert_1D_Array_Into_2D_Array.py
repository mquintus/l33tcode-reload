# 2022 - Convert 1D Array Into 2D Array
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        new = []
        for row in range(m):
            new.append(original[row*n:(row+1)*n])
        return new
