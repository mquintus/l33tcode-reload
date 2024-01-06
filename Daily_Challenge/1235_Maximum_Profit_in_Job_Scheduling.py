# 1235 - Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))

        dp = [-1] * n

        def get_next_index(i):
            target = endTime[i]
            start = i + 1
            end = n - 1
            prev_mid = -1
            while start < end:
                mid = (start + end) // 2
                if mid == prev_mid:
                    return mid
                #print(start, mid, end)
                if startTime[mid - 1] < target and startTime[mid] >= target:
                    return mid
                elif startTime[mid] < target:
                    start = mid + 1
                elif startTime[mid] >= target:
                    end = mid
                prev_mid = mid
            return start


        # take or skip
        curr_end = 0
        def solve(i):
            if i >= n:
                return 0
            if i == n-1:
                return profit[i]
            if dp[i] != -1:
                return dp[i]


            job_start = startTime[i]

            max_profit = 0
            # skip
            skip_profit = solve(i + 1)
            max_profit = max(max_profit, skip_profit)

            # take
            job_profit = profit[i]
            next_index = get_next_index(i)
            if next_index == i or startTime[next_index] < endTime[i]:
                take_profit = job_profit + solve(next_index+1)
            else:
                take_profit = job_profit + solve(next_index)
            max_profit = max(max_profit, take_profit)
            
            dp[i] = max_profit
            return dp[i]
        return solve(0)


