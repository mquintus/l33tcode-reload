# 498 - Diagonal Traverse
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dirs = [(1,-1),(-1,1)]
        d = 0
        rows = len(mat)
        cols = len(mat[0])
        r = 0
        c = 0

        answer = []
        while r < rows and c < cols:
            answer.append(mat[r][c])
            #print(r,c,dirs[d],mat[r][c])
            if r == (rows-1) and c == (cols-1):
                break
            elif r == (rows-1) and d == 1:
                c += 1
                d = 0
            elif c == (cols-1) and d == 0:
                r += 1
                d = 1
            elif r == 0 and d == 0:
                c += 1
                d = 1
            elif c == 0 and d == 1:
                r += 1
                d = 0
            else:
                r += dirs[d][1]
                c += dirs[d][0]
                #print("ADDING",dirs[d],(r,c,))
        return answer
