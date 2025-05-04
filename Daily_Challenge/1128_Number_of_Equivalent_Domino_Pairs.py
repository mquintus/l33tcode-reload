# 1128 - Number of Equivalent Domino Pairs
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        someSet = dict()
        pairCount = 0
        for a,b in dominoes:
            key = (min(a,b),max(a,b))
            if key in someSet:
                someSet[key] += 1
                pairCount += someSet[key]
            else:
                someSet[key] = 0
        return pairCount
