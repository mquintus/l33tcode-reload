class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0:
            return .5
        if n <= 50:
            return .625

        if n >= 4800:
            return 1

        servings = [(100,0), (75,25), (50,50), (25,75)]
        def solve(A, B, dp):
            if A <= 0 and B <= 0:
                return .5
            if A <= 0 and B > 0:
                return 1.
            if A > 0 and B <= 0:
                return 0.
                
            if dp[A][B] != -1:
                return dp[A][B]
            
            probability = 0.0
            for servA,servB in servings:
                probability += solve(A - servA, B - servB, dp)
            dp[A][B] = probability / 4
            return dp[A][B]

        dp = [[-1 for _ in range(4800)] for _ in range(4800)]
        return solve(n,n,dp)
