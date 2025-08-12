# 2787 - Ways to Express an Integer as Sum of Powers
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        Mod = 1_000_000_007
        numbers = []
        for base in range(1,n+1):
            smth = base ** x
            if smth > n: break
            numbers.append(smth)

        dp = [[-1 for _ in range(len(numbers)+1)] for _ in range(n+1)]

        def number_of_ways(i, val):
            if val > n: return 0
            if val == n: return 1
            if i >= len(numbers): return 0
            #print(val, i)
            if dp[val][i] != -1: return dp[val][i]
            take = number_of_ways(i+1, val+numbers[i]) 
            #if take > 0:
            #    print("If you are at",val,"and take",numbers[i], "there is a way")
            skip = number_of_ways(i+1, val) 
            dp[val][i] = (take + skip) % Mod
            return dp[val][i]

        return number_of_ways(0,0)
