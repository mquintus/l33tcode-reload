# 2326 - Spiral Matrix IV
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        d = 0

        row = 0
        col = 0
        minrow = 0
        maxrow = m
        mincol = 0
        maxcol = n
        while head is not None:
            matrix[row][col] = head.val
            head = head.next

            row += directions[d][0]
            col += directions[d][1]

            eol = False
            
            if row >= maxrow:
                maxcol -= 1
                eol = True
            elif row < minrow:
                mincol += 1
                eol = True
            elif col >= maxcol:
                minrow += 1
                eol = True
            elif col < mincol:
                maxrow -= 1
                eol = True
            else:
                eol = False
     
            if eol:
                row -= directions[d][0]
                col -= directions[d][1]
                d = (d + 1) % 4
                row += directions[d][0]
                col += directions[d][1]

        return matrix

