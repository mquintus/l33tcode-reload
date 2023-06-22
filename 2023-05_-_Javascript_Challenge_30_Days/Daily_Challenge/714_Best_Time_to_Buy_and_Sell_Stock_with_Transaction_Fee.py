class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        Sounds like a stack problem or a two pointer problem.

        Starting at the left, 
        Buying should be updated to the smallest element i
        until an element of j > i + fee is found.

        Then selling should be delayed while the price is increasing.
        until the price drops
        '''

        def stateful_approach(prices: List[int], fee: int) -> int:
            sold_state = 0
            bought_state = -100000
            
            for price in prices:
                bought_state = max(bought_state, sold_state + -1 * price)
                sold_state = max(sold_state, bought_state + price - fee)

            return sold_state

        return stateful_approach(prices, fee) 
