# 1208 - Get Equal Substrings Within Budget
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        p0 = 0
        p1 = 0
        currCost = cost[0]
        bestLen = 0
        while p1 < n:
            if currCost > maxCost:
                currCost -= cost[p0]
                p0 += 1
            if p1 < p0:
                p1 = p0
                if p1 == n:
                    break
                currCost = cost[p0]
            if currCost <= maxCost:
                bestLen = max(bestLen, p1-p0+1)
                p1 += 1
                if p1 == n:
                    break
                currCost += cost[p1]
                if currCost <= maxCost:
                    bestLen = max(bestLen, p1-p0+1)
        return bestLen


