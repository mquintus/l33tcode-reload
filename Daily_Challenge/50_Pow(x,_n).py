class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == True:
                return -1
            else:
                return 1


        orig_n = n
        n = abs(n)
        
        exp = 1
        res = {}
        res[1] = x

        while exp < n:
            res[exp * 2] = res[exp] * res[exp]
            exp = exp * 2

        while abs(exp) > abs(n):
            minemp = 1
            maxemp = exp - n
            for somexp in range(maxemp, minemp - 1, -1):
                if somexp in res:
                    res[exp - somexp] = res[exp] / res[somexp]
                    exp = exp - somexp
                    break

        if orig_n < 0:
            res[n] = 1 / res[n]

        return res[n]
