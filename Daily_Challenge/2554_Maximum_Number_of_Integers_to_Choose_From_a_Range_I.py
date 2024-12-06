# 2554 - Maximum Number of Integers to Choose From a Range I
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = [False for _ in range(n+2)]
        for b in banned:
            if b <= n:
                ban[b] = True
        # take or skip
        allowed = [i for i in range(1,n+1) if not ban[i]]
        m = len(allowed)

        @cache
        def dp(i, prevsum):
            #print(i, prevsum)
            if prevsum == maxSum: return 0
            if i == m: return 0
            nextsum = allowed[i] + prevsum
            if nextsum == maxSum: return 1
            if nextsum > maxSum: return 0
            # take
            take = 1 + dp(i+1, nextsum)
            # skip
            #skip = dp(i+1, prevsum)
            #print("take",take,"skip",skip)
            return take
        return dp(0,0) 


