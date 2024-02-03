# 1043 - Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n

        # take or skip
        @cache
        def solve(pos):
            if pos >= n:
                return 0
            bestoption = -1
            for length in range(1, k+1):
                if pos+length > n:
                    break
                take = solve(pos + length) + length*max(arr[pos:pos+length])
                #print(pos, length, take)
                bestoption = max(bestoption, take)
            return bestoption
        
        return solve(0)
