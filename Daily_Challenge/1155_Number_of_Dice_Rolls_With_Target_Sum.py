# 1155 - Number of Dice Rolls With Target Sum
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        dp = [[-1] * 1001 for _ in range(31)]

        def get_ways(iteration, value):
            #print(iteration, value)
            if value == 0 and iteration == 0:
                return 1
            if value <= 0:
                return 0
            if iteration <= 0:
                return 0
            if dp[iteration][value] != -1:
                return dp[iteration][value]

            all_ways = 0
            for possible_k in range(min(k,value), 0, -1):
                ways = get_ways(iteration - 1, value - possible_k)
                #print("iteration, possible_k, ways", iteration, possible_k, ways)
                all_ways += ways
            
            dp[iteration][value] = all_ways % MOD
            return dp[iteration][value]


        return get_ways(n, target)

