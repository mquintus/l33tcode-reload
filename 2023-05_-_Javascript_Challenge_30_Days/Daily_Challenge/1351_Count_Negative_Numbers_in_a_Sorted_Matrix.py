class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        Since the matrix is sorted, we can use binary search to find numbers smaller than zero.
        We know that for each row/column to the right/bottom only smaller numbers can be found.
        So the naive solution is to start anywhere in the matrix and "walk" towards zero or -1. 
        If we find a negative number at position i,j, we know that all numbers right and below that position are also negative.
        
        The solution will have a dominant direction (horizontal) and a secondary direction (vertical).
        
        We start at position 0,n.
        If it is negative, we walk left.
        If it is not negative, then we search downwards.
        
        If we find a negative number at i,0 we know that all cells >i,>0 are negative
        Since we start at the top right corner, and only ever move left, 
        to avoid double counting, we only count the negatives below:
        counter += (m - j)

        If no negative number was found, we iterate by one row downwards 
        if the cell is negative, we iterate all columns back to the left until an non-negative number is found.

        As mentioned before.
        We will use a counter.
        Whenever we find a negative number, we will count all cells below.
        '''

        def left_right_walk_solution(grid: List[List[int]]) -> int:
            n = len(grid[0])
            m = len(grid)

            if m == 0 or n == 0:
                return 0

            negative_count = 0

            prev_number = "positive"
            direction = "start"
            i = n - 1
            j = 0
            # print(j,i,m,n)
            while i < n and i >= 0 and j < m and j >= 0:
                curr_number = grid[j][i]
                #print(i,j, curr_number)
                
                
                if curr_number < 0:
                    negative_count += m - j

                if curr_number < 0:
                    direction = 'left'
                    i -= 1
                    continue
                
                if curr_number >= 0:
                    direction = 'down'
                    j += 1
                    continue
                
            return negative_count
        return left_right_walk_solution(grid)         



            
