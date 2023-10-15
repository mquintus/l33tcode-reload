# 1269 - Number of Ways to Stay in the Same Place After Some Steps
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # If the only valid field is the origin, 
        # the only valid move is STOP * steps
        if arrLen == 1:
            return 1
        if steps == 1:
            return 1
        if steps == 2:
            return 2

        MOD = 10**9+7

        ## No valid solution has more positions than steps.
        # Actually, for a solution to be valid, the maximum distance from the home square 
        # is steps // 2 
        # because you have to go there and return within `steps` rounds, 
        # that is, you can only go half the way before you have to return.
        dp = [[-1 for _ in range(steps + 1)] for _ in range(min(steps // 2, arrLen) + 2)]


        def solve(pos, remain):
            if dp[pos][remain] != -1:
                return dp[pos][remain]
            if remain == 0 and pos == 0:
                return 1 # let's terminate here
            if remain < pos:
                return -1 # not enough steps to return home
            if remain == pos:
                return 1 # just go home.
            if remain == 0:
                return -1 # no steps: no further options

            left = 0
            right = 0
            stop = solve(pos, remain - 1) 

            if pos > 0:
                left = solve(pos - 1, remain - 1)
                if left < 0:
                    left = 0

            if stop < 0:
                stop = 0          
            
            if pos < arrLen - 1:
                right = solve(pos + 1, remain - 1)
                if right < 0:
                    right = 0

            dp[pos][remain] = (left + right + stop) % MOD
            return dp[pos][remain]

        return solve(0, steps) 

                 


