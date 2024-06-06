# 846 - Hand of Straights
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from sortedcontainers import SortedDict 
        #hand.sort()
        handCounts = SortedDict(Counter(hand))
        for card, count in handCounts.items():
            if count == 0:
                continue
            for i in range(card, card+groupSize):
                if i not in handCounts.keys() or handCounts[i] < count:
                    return False
                handCounts[i] -= count
        return True
