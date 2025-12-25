# 3075 - Maximize Happiness of Selected Children
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total = 0
        dec = 0
        for h in happiness[::-1]:
            if dec >= h:
                h = 0
            else:
                h -= dec
            #print("Adding h", h)
            total += h 
            if k > 1:
                dec += 1
                k -= 1
            else: 
                break
        return total

