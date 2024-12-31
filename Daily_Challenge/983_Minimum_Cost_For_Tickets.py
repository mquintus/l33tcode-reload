# 983 - Minimum Cost For Tickets
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * 366
        dp[0] = 0
        duration = [1,7,30]

        if len(days) == 0:
            return 0

        i = 0
        for day in range(1, 366):
            if day < days[i]:
                dp[day] = dp[day-1]
                continue
            
            i += 1
            dp[day] = float('inf')
            for tariff in [0,1,2]:
                prevday = max(0, day-duration[tariff])
                dp[day] = min(dp[day], dp[prevday] + costs[tariff])

            if i == len(days):
                #i -= 1
                break
        
        return dp[day]
