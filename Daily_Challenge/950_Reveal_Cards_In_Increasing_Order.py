# 950 - Reveal Cards In Increasing Order
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        newdeck = [i for i in range(n)]
        newsort = []
        while newdeck:
            newsort.append(newdeck.pop(0))
            if newdeck:
                newdeck.append(newdeck.pop(0))

        newdeck = [0 for i in range(n)]
        for i in range(n):
            newdeck[newsort[i]] = deck[i]

        return newdeck
