# 2742 - Painting the Walls
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # We want the paid painter to select the walls 
        # with the lowest cost and longest time
        
        dp = [[0] * (len(cost) + 1) for _ in range((len(cost) + 1))]
        for i in range(1, len(cost) + 1):
            dp[len(cost)][i] = 500 * 10**6  + 1

        for i in range(len(cost) -1, -1, -1):
            for time_covered in range(1, len(cost)+1):
                skip = dp[i+1][time_covered] # use free painter
                take = cost[i] + dp[i+1][max(0, time_covered - 1 - time[i])] # pay for it
                res = min(take, skip)
                dp[i][time_covered] = res 

        return dp[0][len(cost)]
