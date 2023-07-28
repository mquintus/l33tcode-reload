class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        '''
        The current player will win, if the next player won't.

        There are only 20 numbers in the array, this should be manageable with brute force recursion.
        isWinner(n) = ~isWinner(n + 1)

        Let's have a counter, maximizing the score in each round, alternating the perspective each round.
        '''

        def isWinner(nums, prev_points):
            if len(nums) == 0:
                return prev_points

            if len(nums) == 1:
                return isWinner([], -prev_points + nums[0])

            if len(nums) > 1:
                take_first = -1 * isWinner(nums[1:], -prev_points + nums[0])
                take_last = -1 * isWinner(nums[:-1], -prev_points + nums[-1])
                wins = max(take_first, take_last)
                return wins

        return 0 <= isWinner(nums, 0)
