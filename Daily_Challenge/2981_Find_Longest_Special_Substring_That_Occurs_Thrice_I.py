# 2981 - Find Longest Special Substring That Occurs Thrice I
class Solution:
    def maximumLength(self, s: str) -> int:
        maxlengths = {}
        prev = ""
        bestval = -1
        for el in s: 
            if el == prev:
                maxlengths[el].append(maxlengths[el][-1] + 1)
                if maxlengths[el][-1] >= 3:
                    goodval = maxlengths[el][-1] - 2
                    bestval = max(bestval, goodval)
            else:
                if el not in maxlengths:
                    maxlengths[el] = []
                maxlengths[el].append(1)
            prev = el
        
        for key, amounts in maxlengths.items():
            if len(amounts) < 3: continue
            amounts.sort()
            goodval = min(amounts[-3:])
            bestval = max(bestval, goodval)
        
        return bestval
