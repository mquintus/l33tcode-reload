# 629 - K Inverse Pairs Array
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def f(n,k):
            if k == 0:
                return 1
            if k < 0:
                return 0
            if n <= 0:
                return 0
            if n == 1:
                return 0
            if n == 2:
                if k < 2:
                    return 1
                else:
                    return 0
            if n == 3:
                if k == 0:
                    return 1
                if k == 1:
                    return 2
                if k == 2: # 3,1,2 
                    return 2
                if k == 3:
                    return 1 # 3,2,1
                if k > 3:
                    return 0
            if n == 4:
                if k == 2:
                    return 5
                if k == 3:
                    return 6
                if k == 5:
                    return 3
                if k == 6:
                    return 1
                if k > 6:
                    return 0
                

            totalsum = 0
            #for i in range(0, n-1):
            totalsum = f(n-1,k) + f(n,k-1) - f(n-1, k-n)

            return totalsum % MOD
        return f(n,k)
