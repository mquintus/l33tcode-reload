# 2561 - Rearranging Fruits
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        a = Counter(basket1)
        b = Counter(basket2)
        to_swap = []
        for k,v in a.items():
            if k not in b:
                b[k] = 0
            if (v + b[k])%2 == 1:
                return -1
            if v < b[k]:
                to_swap.extend([k] * ((b[k]-v)//2))
            elif v > b[k]:
                to_swap.extend([k] * ((v-b[k])//2))

        for k,v in b.items():
            if k not in a:
                a[k] = 0
                if (v + a[k])%2 == 1:
                    return -1
                to_swap.extend([k] * ((v)//2))
        
        to_swap.sort()
        cost = 0
        n = len(to_swap)
        smallestElement1 = min(basket1)
        smallestElement2 = min(basket2)
        smallestElement = min(smallestElement1,smallestElement2)
        for i in range(n//2):
            cost += min(smallestElement*2, to_swap[i])
        return cost
