# 2516 - Take K of Each Character From Left and Right
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        if len(s) < 3*k:
            return -1

        matching = 0
        c = {'a':0, 'b':0, 'c':0}
        for el in s:
            c[el] += 1
            if c[el] == k:
                matching += 1
        
        if matching < 3:
            return -1

        if len(s) == 3*k:
            return 3*k

        def red(p):
            el = s[p]
            if c[el] == k:
                nonlocal matching
                matching -= 1
            c[el] -= 1

        def inc(p):
            el = s[p]
            c[el] += 1
            if c[el] == k:
                nonlocal matching
                matching += 1

        p0 = 0
        p1 = -1
        n = len(s)
        maxsub = 0
        while p0 < n and p1 < n: 
            if matching == 3:
                p1 += 1
                if p1 == n:
                    break
                red(p1)
            else:
                inc(p0)
                p0 += 1
                if p0 > p1:
                    p1 += 1
                    if p1 == n:
                        break
                    red(p1)
            if matching == 3:
                sol = p1-p0
                #print(p0,p1,sol, s[p0:p1+1])
                if sol > maxsub:
                    maxsub = sol
        return n-maxsub-1


