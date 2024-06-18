# 826 - Most Profit Assigning Work
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        workers = sorted(Counter(worker).items())
        dp = sorted(list(zip(difficulty, profit)))

        payoff = 0

        if len(dp) == 0:
            return 0

        highest_profit_job = 0
        for skill, count in workers:
            if len(dp) > 0:
                easiest_job, someprofit = dp[0]
                while easiest_job <= skill:
                    highest_profit_job = max(highest_profit_job, someprofit)
                    dp.pop(0)
                    if len(dp) == 0:
                        break
                    easiest_job, someprofit = dp[0]
            payoff += highest_profit_job * count
        return payoff
