# 1760 - Minimum Limit of Balls in a Bag
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def checkPenalty(p):
            neededOperations = 0
            for el in nums:
                if el <= p: continue
                #if neededOperations > maxOperations: return False
                neededOperations -= (-el + p) // p
            return neededOperations <= maxOperations

        minPenalty = 1
        maxPenalty = max(nums)
        assumedPenalty = (maxPenalty + minPenalty)//2
        while minPenalty < maxPenalty:
            assumedPenalty = (maxPenalty + minPenalty)//2
            if checkPenalty(assumedPenalty):
                if assumedPenalty == 1 or not checkPenalty(assumedPenalty-1):
                    return assumedPenalty
                maxPenalty = assumedPenalty
            else:
                if checkPenalty(assumedPenalty+1):
                    return assumedPenalty+1
                else:
                    minPenalty = assumedPenalty+1
        return assumedPenalty

            
