# 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        '''
        This challenge is about keeping track of a threshold value
        and gradually increasing it. 
        '''
        mod = 10**9+7

        if k == 0:
            # No way for search cost to be 0
            # because n is always at least 1
            return 0

        # If the number range is smaller that the threshold events,
        # there is no possible solution
        if m < k:
            return 0
        # If the number of integers is smaller that the threshold events,
        # there is no possible solution
        if n < k:
            return 0

        # There is only one solution (of increasing numbers) if n == m == k
        if n == m == k:
            return 1

        if n == k:
            # We have a bigger range of numbers so there is lots of flexibility,
            # but since n == k, we have to have an linearly increasing sequence.
            # 
            if m == n + 1:
                # If we e.g. have one number(m) more available than spots(n)
                # The variance here is which number of m to skip
                return m
            if m > n:
                # If we have two or more numbers (m) available, we can skip any
                # pair of them (without re-drawing)

                # Free positions = m-n
                return (math.factorial(m) // (math.factorial(m-n) * math.factorial(m - (m-n))))%mod

        # If the length of the sequence is larger than the number of thresholds, things get interesting.
        if n > k:
            # Let's first consider that we only have 1 steps. 
            # That means that all numbers must be the same
            if k == 1:
                # So we choose the first element (any out of m)
                # and we can't change it anymore?
                # Wrong, we'd have to start with the highest element, then
                # any following sequence would suffice.
                # The formula for any permutation of numbers is len_array ^ pool_of_items
                # The first element though is fixed as the largest element
                # so the length of the sequence is n-1, so the formula
                # in our case is m^(n - 1)
                part_of_the_solution = m**(n-1)
                # and then, actually, we could start with a smaller element and just not use
                # the highest element at all
                for mi in range(m):
                    part_of_the_solution += mi**(n-1)
                return part_of_the_solution % mod

            # Let's assume we have 2 steps or more
            # and solve this iteratively / dynamic programming.
            dp = [[[-1] * (k+3) for _ in range(m+3)] for _ in range(n+3)]
            #print(dp)
            def solve(i, threshold, cost, m, dp):
                #print("Visiting", i, threshold, cost)
                if dp[i][threshold][cost] != -1:
                    return dp[i][threshold][cost]
                if i == 1:
                    if cost == 1:
                        return 1
                    else:
                        return 0
                if cost == 0:
                    return 0
                if i == 1:
                    return 0
                    
                number_of_ways = 0
                for j in [*range(m, threshold, -1), *range(threshold, 0, -1)]:
                    if j <= threshold:
                        number_of_ways += solve(i-1, threshold, cost, m, dp)
                    else:
                        number_of_ways += solve(i-1, j, cost - 1, m, dp)
                dp[i][threshold][cost] = number_of_ways % mod
                return dp[i][threshold][cost]
            result = 0
            for j in range(1, m+1):
                r = solve(n, j, k, m, dp)
                result += r
                result %= mod
            return result % mod
