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
