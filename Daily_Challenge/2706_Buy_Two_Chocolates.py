# 2706 - Buy Two Chocolates
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        '''
        Intuition: Find the two smallest numbers.
        If their sum is smaller or equal the money,
        return the difference.
        Otherwise return the money.
        '''
        small1 = 101
        small2 = 101
        for p in prices:
            if p <= small1:
                small2 = small1
                small1 = p
            elif p <= small2:
                small2 = p

        difference = money - small1 - small2
        if difference >= 0:
            return difference
        return money
