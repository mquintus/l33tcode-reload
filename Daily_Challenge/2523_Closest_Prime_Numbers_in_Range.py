# 2523 - Closest Prime Numbers in Range
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left <= 2 and right >= 3: return [2,3]
        if left <= 3 and right >= 5: return [3,5]
        pl = [True]*(right+2)
        pl[0] = False
        pl[1] = False
        base = 1
        while base < len(pl) and base < right:
            while base < len(pl) and pl[base] == False:
                base += 1
            #print(2*base, right, base)
            for i in range(2*base, right+2, base):
                pl[i] = False
            base += 1

        #print(pl)
        #return [-1,-1]
        p = [i for i, el in enumerate(pl) if el == True]

        #print(p)

        l = bisect.bisect_left(p, left)
        while l < len(p) and p[l] < left:
            l += 1
        if l == len(p): return [-1,-1]
        prev = p[l]
        l += 1
        mind = 10000000
        res = [-1,-1]
        while l < len(p) and p[l] <= right:
            d = p[l] - prev
            #print(d, p[l], prev)
            if d == 1 or d == 2:
                return [prev, p[l]]
            if d < mind:
                mind = d
                res = [prev, p[l]]
            prev = p[l]
            l += 1
        return res
