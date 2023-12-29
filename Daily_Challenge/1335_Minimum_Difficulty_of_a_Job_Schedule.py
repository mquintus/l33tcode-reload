# 1335 - Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        The jobs are sequential, so basically the question is
        how to split the list into `d` lists,
        such that the max() of each sublist is minimized 
        '''
        jobs = len(jobDifficulty)
        dp = [[-1] * (d+1) for _ in range(jobs + 1)]

        #smth = [i  for i in range(300)]
        #random.shuffle(smth)
        #print(smth.__str__().replace(' ', ''))

        def solve(pointer1, remainingDays):
            if dp[pointer1][remainingDays] != -1:
                return dp[pointer1][remainingDays]
            if remainingDays == 0:
                dp[pointer1][remainingDays] = max(jobDifficulty[pointer1:])
                #print("On the last day:", dp[pointer1][remainingDays])
                return dp[pointer1][remainingDays]
            allCost = float('inf')
            for pointer2 in range(pointer1+1, jobs - remainingDays + 1):
                cost_now = max(jobDifficulty[pointer1:pointer2])
                cost_then = solve(pointer2, remainingDays - 1)
                #print(pointer2, cost_now, cost_then)
                cost = cost_now + cost_then
                allCost = min(cost, allCost)

            dp[pointer1][remainingDays] = allCost
            return allCost 

        result = solve(0, d - 1)
        if result == float('inf'):
            return -1
        return result
