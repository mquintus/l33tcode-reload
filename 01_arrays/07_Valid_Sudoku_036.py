class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Sounds like an easy one. 
        Here is what we know:
        - There are three types of validation:
          a) Horizontal
          b) Vertical
          c) Sub-Box
        
        - And the validation method is basically that taken a list of numbers to validate,
          there are not duplicates.

        - Approach: 
          a) Helper function for each validation type
             b) plus a general helper function that always does the same check: no duplicates
          b) If one of the test fails, return False
        '''
        def check_any(mylist):
            chars = set(mylist)
            for c in chars:
                if c != '.':
                    if mylist.count(c) > 1:
                        return False
            return True

        def check_horizontal(board):
            success = True
            for line in board:
                success &= check_any(line)
                if not success:
                    return False
            return success

        def check_vertically(board):
            success = True
            for i in range(len(board[0])):
                myline = [line[i] for line in board]
                success &= check_any(myline)
                if not success:
                    return False
            return success

        def check_subbox(board):
            success = True
            for x in range(3):
                for y in range(3):
                    mylist = []
                    for xi in range(3):
                        for yj in range(3):
                            mylist.append(board[x*3 + xi][y* 3 + yj])
                    success &= check_any(mylist)
                    if not success:
                        return False
            return success
        
        return check_horizontal(board) & check_vertically(board) & check_subbox(board)
