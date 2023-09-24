# 799 - Champagne Tower
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        The 0th glass in each row gets 1/2**n of each additional pour.

        If all glasses above a particular row are full, the amount flowing 
        through that row is related to pascal's triangle.
        '''
        dp = [[0] * 102 for _ in range(102)] 
        dp[0][0] = poured

        for row in range(1, query_row + 1):
            for glass in range(0, row + 1):
                rest = max(0, dp[row - 1][glass] - 1) / 2
                dp[row][glass] += rest
                if glass > 0:
                    rest = max(0, dp[row - 1][glass - 1] - 1) / 2
                    dp[row][glass] += rest
                
        return min(1, dp[query_row][query_glass])


        
        
